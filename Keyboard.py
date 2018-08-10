# Adapted from http://www.hackerthreads.org/Topic-42395 for the hook
import ctypes
from ctypes import wintypes
import atexit
import traceback
import time

from structs import *
from functions import *
from KeyboardLCID import *
from codes.KbdScanCode import *
from codes.InputConst import *
from KeyboardEvent import KeyboardEvent, parseEvent

OUTPUT_FILENAME = "kbdInputs.yapam"

# Variables for the hook
AltGrPressed = False 
ignoreExtraAltRight = False 
lt_shiftVK = [VK_SHIFT, VK_LSHIFT, VK_RSHIFT]
lt_altVK = [VK_MENU, VK_RMENU, VK_LMENU]
lt_ctlVK = [VK_CONTROL, VK_LCONTROL, VK_RCONTROL]

LLKHF_INJECTED = 0x00000010

KEY_DOWN = 'DOWN'
KEY_UP = 'UP'

keyboard_eventTypes = { 
    WM_KEYDOWN: KEY_DOWN, 
    WM_KEYUP: KEY_UP, 
    WM_SYSKEYDOWN: KEY_DOWN, 
    WM_SYSKEYUP: KEY_UP, 
}

def checkKeyPressedDown(lt_vk):
    for vk in lt_vk:
        if bool(GetKeyState(vk) & 0x8000):
            return True
    return False

def basicPrintHook(e):
    print(e)
    return True

def noFunction(event):
    return True
    
def writeToFileEvents(event):
    with open(OUTPUT_FILENAME, "a") as f:
        f.write(str(event) + "\n")
    return True

class Keyboard():
    
    def __init__(self):
        self.k = KeyboardLCID()
        self.KbdLayout = self.k.GetKeyboardInfo()
    
    def PressNReleaseKey(self, hexKeyCode):
        self.PressKey(hexKeyCode)
        self.ReleaseKey(hexKeyCode)
    
    def PressKey(self, hexKeyCode):
        x = self.__doInputObject(hexKeyCode)
        SendInputFunc(1, ctypes.byref(x), ctypes.sizeof(x))

    def ReleaseKey(self, hexKeyCode):
        x = self.__upInputObject(hexKeyCode)
        SendInputFunc(1, ctypes.byref(x), ctypes.sizeof(x))
        
    def SendUnicodeChar(self, unicodeCode):
        x = self.__unInputObject(unicodeCode)
        SendInputFunc(1, ctypes.byref(x), ctypes.sizeof(x))
    
    # Key down
    def __doInputObject(self, hexKeyCode):
        return INPUT(type=INPUT_KEYBOARD, ki=KEYBDINPUT(wVk=hexKeyCode))
    
    # Key up
    def __upInputObject(self, hexKeyCode):
        return INPUT(type=INPUT_KEYBOARD, ki=KEYBDINPUT(wVk=hexKeyCode,dwFlags=KEYEVENTF_KEYUP))
    
    # Unicode
    def __unInputObject(self, unicodeCode):
        return INPUT(type=INPUT_KEYBOARD, ki=KEYBDINPUT(wScan=unicodeCode,dwFlags=KEYEVENTF_UNICODE))
                          
    # Take a string and use send_input to simulate the typing
    def InputText(self, stre):
        lt_inputs = []
        for ch in stre.replace('\r\n', '\r').replace('\n', '\r'):
            if ch == "\n": # Newline seems to be broken even with this
                lt_inputs.append(self.__doInputObject(VK_RETURN))
                continue

            res, hexKey = VkKeyScanEx(ch, self.k.KeyboardLayout)
            stackUp = []
            if res == -1 and hexKey == -1:
                lt_inputs.append(self.__unInputObject(ord(ch)))
            else:
                if res & SHIFT_KEY:
                    lt_inputs.append(self.__doInputObject(VK_SHIFT))
                    stackUp.append(self.__upInputObject(VK_SHIFT))
                if res & CTRL_KEY:
                    lt_inputs.append(self.__doInputObject(VK_CONTROL))
                    stackUp.append(self.__upInputObject(VK_CONTROL))
                if res & ALT_KEY:
                    lt_inputs.append(self.__doInputObject(VK_MENU))
                    stackUp.append(self.__upInputObject(VK_MENU))
                if res & HANKAKU_KEY:
                    print("Not gonna support that key, sorry : Hankaku")
                if res & RESERVED_KEY[0] or res & RESERVED_KEY[1]:
                    print(res, " This is a reserved key, should not see this text")
                lt_inputs = lt_inputs + [self.__doInputObject(hexKey)] + stackUp[::-1]

        input_array = (INPUT * len(lt_inputs))(*lt_inputs)
        SendInputFunc(len(lt_inputs), ctypes.byref(input_array[0]), ctypes.sizeof(INPUT))

    def __hooking_keyboard(self, callback):    
        def process_key(eventType, vk, scanCode, isExtended):
            global AltGrPressed, ignoreExtraAltRight

            # AltGr generates an extra "right alt" event
            if vk == VK_RMENU and ignoreExtraAltRight:
                ignoreExtraAltRight = False
                return True
                
            shiftPressed = checkKeyPressedDown(lt_shiftVK)
            altPressed   = checkKeyPressedDown(lt_altVK)
            ctrlPressed  = checkKeyPressedDown(lt_ctlVK)

            modifiersState = {
                'SHIFT'    : shiftPressed,
                'ALT'      : altPressed,
                'CTRL'     : ctrlPressed,
                'ALTGR'    : AltGrPressed,
                'NUMLOCK'  : GetKeyState(VK_NUMLOCK) & 1,
                'CAPSLOCK' : GetKeyState(VK_CAPITAL) & 1,
                'SCRLOCK'  : GetKeyState(VK_SCROLL) & 1
            }            
            name = list(GetKeyNameText(vk, scanCode, isExtended, modifiersState))

            # Better way handle this has to exist
            # on EN-US and CAN-FR, this is not seen, further investigation required
            if scanCode == 541 and vk == VK_LCONTROL:
                ignoreExtraAltRight = True
                AltGrPressed = eventType == KEY_DOWN

            isKeypad = (vk in lt_Numpad) or ((scanCode, vk, isExtended) in lt_OtherNumpad)
            event = KeyboardEvent(eventType=eventType, vk=vk, name=name, modifiers=modifiersState, isKeypad=isKeypad)
            return callback(event)

        def low_level_keyboard_handler(nCode, wParam, lParam):
            try:
                vk = lParam.contents.vk_code
                # Ignore the second 'alt' DOWN observed in some cases.
                fake_alt = (LLKHF_INJECTED | 0x20)
                
                # Ignore events generated by SendInput with Unicode.
                if vk != VK_PACKET and lParam.contents.flags & fake_alt != fake_alt:
                    eventType = keyboard_eventTypes[wParam]
                    isExtended = lParam.contents.flags & 1
                    scanCode = lParam.contents.scan_code
                    should_continue = process_key(eventType, vk, scanCode, isExtended)
                    if not should_continue:
                        return -1
            except Exception as e:
                print('Error in keyboard hook:')
                traceback.print_exc()

            return CallNextHookEx(None, nCode, wParam, lParam)

        keyboardCallback = LowLevelKeyboardProc(low_level_keyboard_handler)
        handle =  ctypes.c_int(0)
        thread_id = wintypes.DWORD(0)
        keyboard_hook = SetWindowsHookEx(WH_KEYBOARD_LL, keyboardCallback, handle, thread_id)

        atexit.register(UnhookWindowsHookEx, keyboardCallback)

    def listen(self, callback=noFunction):
        self.__hooking_keyboard(callback)
        msg = LPMSG()
        while not GetMessage(msg, 0, 0, 0):
            TranslateMessage(msg)
            DispatchMessage(msg)
            
    def __GetEventsFromFile(self, filename):
        with open(filename) as f:
            data = f.read().split('\n')

        lt = []
        last_time = parseEvent(data[0], 0)[1]
        for x in data:
            if x == '':
                continue
            event, last_time = parseEvent(x, last_time)
            if event != None:
                lt.append(event)
            else:
                print("Line not formated correctly : {}")
        return lt
                
    def DoInputsRespectDelay(self, filename):
        lt = self.__GetEventsFromFile(filename)
        for event in lt:
            if event.eventType == KEY_DOWN:
                self.PressKey(event.vk)
            elif event.eventType == KEY_UP:
                self.ReleaseKey(event.vk)
            time.sleep(event.time)
    
    def FastInputs(self, filename):
        lt = self.__GetEventsFromFile(filename)
        for event in lt:
            if event.eventType == KEY_DOWN:
                self.PressKey(event.vk)
            elif event.eventType == KEY_UP:
                self.ReleaseKey(event.vk)
        
if __name__ == "__main__":
    # TESTS
    k = Keyboard()
    time.sleep(3)
    with open("text.txt") as f:
        data = f.read()
    k.listen(writeToFileEvents)
    #k.FastInputs(OUTPUT_FILENAME)
    #k.InputText(data)
    