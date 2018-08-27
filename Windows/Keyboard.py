'''
Keyboard interface
'''
#pylint: disable=unused-wildcard-import
#pylint: disable=wildcard-import
#pylint: disable=unused-argument

import ctypes
from ctypes import wintypes
import atexit
import time

from .Structs import *
from .Functions import *
from .codes.KbdScanCode import *
from .codes.InputConst import *
from .KeyboardEvent import KeyboardEvent, parseEvent

OUTPUT_FILENAME = "kbdInputs.yapam"

SEND_INPUT = lambda x: SendInputFunc(1, ctypes.byref(x), ctypes.sizeof(x))

# Variables for the hook
LT_SHIFTVK = [VK_SHIFT, VK_LSHIFT, VK_RSHIFT]
LT_ALTVK = [VK_MENU, VK_RMENU, VK_LMENU]
LT_CTLVK = [VK_CONTROL, VK_LCONTROL, VK_RCONTROL]

KEYBOARD_LAYOUT = lambda: GetKeyboardLayout
LLKHF_INJECTED = 0x00000010

KEY_DOWN = 'DOWN'
KEY_UP = 'UP'

KEYBOARD_EVENT_TYPES = {
    WM_KEYDOWN: KEY_DOWN,
    WM_KEYUP: KEY_UP,
    WM_SYSKEYDOWN: KEY_DOWN,
    WM_SYSKEYUP: KEY_UP}

def basic_print_hook(event):
    '''Print event to the console.'''
    print(event)
    return True

def no_function(event):
    '''.'''
    return True

def write_to_file_events(event):
    '''Function to write the events to the file.'''
    with open(OUTPUT_FILENAME, "a") as file_handle:
        file_handle.write(str(event) + "\n")
    return True

def _get_events_from_file(filename):
    '''TODO'''
    with open(filename) as file_handle:
        data = file_handle.read().split('\n')

    lt_event = []
    last_time = parseEvent(data[0], 0)[1]
    for x_data in data:
        if x_data == '':
            continue
        event, last_time = parseEvent(x_data, last_time)
        if event is not None:
            lt_event.append(event)
        else:
            print("Line not formated correctly : {}")
    return lt_event

def _do_input_object(hex_key_code):
    '''Get a Input obkect for a key down'''
    return INPUT(type=INPUT_KEYBOARD,
                 ki=KEYBDINPUT(wVk=hex_key_code))

def _up_input_object(hex_key_code):
    '''Get a Input obkect for a key up'''
    return INPUT(type=INPUT_KEYBOARD,
                 ki=KEYBDINPUT(wVk=hex_key_code, dwFlags=KEYEVENTF_KEYUP))

def _un_input_object(unicode_code):
    '''Get a Input obkect for unicode'''
    return INPUT(type=INPUT_KEYBOARD,
                 ki=KEYBDINPUT(wScan=unicode_code, dwFlags=KEYEVENTF_UNICODE))

def _check_key_pressed_down(lt_vk):
    '''Get if the key if pressed down'''
    for virtual_key in lt_vk:
        if bool(GetKeyState(virtual_key) & 0x8000):
            return True
    return False

def press_n_release_key(hex_key_code):
    '''Simulate a key down and a key up'''
    press_key(hex_key_code)
    release_key(hex_key_code)

def press_key(hex_key_code):
    '''Send key down'''
    SEND_INPUT(_do_input_object(hex_key_code))

def release_key(hex_key_code):
    '''Send key up'''
    SEND_INPUT(_up_input_object(hex_key_code))

def send_unicode_char(unicode_code):
    '''Send unicode'''
    SEND_INPUT(_un_input_object(unicode_code))


# Take a string and use send_input to simulate the typing
def input_text(stre):
    '''Get the codes for a string, the Send the codes'''
    lt_inputs = []
    for char in stre.replace('\r\n', '\r').replace('\n', '\r'):
        if char == "\n": # Newline seems to be broken even with this
            lt_inputs.append(_do_input_object(VK_RETURN))
            continue

        res, hex_key = VkKeyScanEx(char, KEYBOARD_LAYOUT())
        stack_up = []
        if res == -1 and hex_key == -1:
            lt_inputs.append(_un_input_object(ord(char)))
        else:
            if res & SHIFT_KEY:
                lt_inputs.append(_do_input_object(VK_SHIFT))
                stack_up.append(_up_input_object(VK_SHIFT))
            if res & CTRL_KEY:
                lt_inputs.append(_do_input_object(VK_CONTROL))
                stack_up.append(_up_input_object(VK_CONTROL))
            if res & ALT_KEY:
                lt_inputs.append(_do_input_object(VK_MENU))
                stack_up.append(_up_input_object(VK_MENU))
            if res & HANKAKU_KEY:
                print("Not gonna support that key, sorry : Hankaku")
            if res & RESERVED_KEY[0] or res & RESERVED_KEY[1]:
                print(res, " This is a reserved key, should not see this text")
            lt_inputs = lt_inputs + [_do_input_object(hex_key)] + stack_up[::-1]

    input_array = (INPUT * len(lt_inputs))(*lt_inputs)
    SendInputFunc(len(lt_inputs), ctypes.byref(input_array[0]), ctypes.sizeof(INPUT))

def _hooking_keyboard(callback):
    '''Hooking the keyboard'''
    #pylint: disable=unused-variable
    altgr_pressed, ignore_extra_altright = False, False
    #pylint: enable=unused-variable
    def process_key(event_type, virtual_key, scan_code, is_extended):
        nonlocal altgr_pressed, ignore_extra_altright
        # AltGr generates an extra "right alt" event
        if virtual_key == VK_RMENU and ignore_extra_altright:
            ignore_extra_altright = False
            return True

        shift_pressed = _check_key_pressed_down(LT_SHIFTVK)
        alt_pressed = _check_key_pressed_down(LT_ALTVK)
        ctrl_pressed = _check_key_pressed_down(LT_CTLVK)

        modifiers_state = {
            'SHIFT'    : shift_pressed,
            'ALT'      : alt_pressed,
            'CTRL'     : ctrl_pressed,
            'ALTGR'    : altgr_pressed,
            'NUMLOCK'  : GetKeyState(VK_NUMLOCK) & 1,
            'CAPSLOCK' : GetKeyState(VK_CAPITAL) & 1,
            'SCRLOCK'  : GetKeyState(VK_SCROLL) & 1
        }
        name = list(GetKeyNameText(virtual_key, scan_code, is_extended, modifiers_state))

        # Better way handle this has to exist
        # on EN-US and CAN-FR, this is not seen, further investigation required
        if scan_code == 541 and virtual_key == VK_LCONTROL:
            ignore_extra_altright = True
            altgr_pressed = event_type == KEY_DOWN

        is_keypad = (virtual_key in LT_NUMPAD) or \
                    ((scan_code, virtual_key, is_extended) in LT_OTHER_NUMPAD)

        event = KeyboardEvent(eventType=event_type, vk=virtual_key, name=name,
                              modifiers=modifiers_state, isKeypad=is_keypad)
        return callback(event)

    def low_level_keyboard_handler(n_code, w_param, l_param):
        virtual_key = l_param.contents.vk_code
        # Ignore the second 'alt' DOWN observed in some cases.
        fake_alt = (LLKHF_INJECTED | 0x20)
        # Ignore events generated by SendInput with Unicode.
        if virtual_key != VK_PACKET and l_param.contents.flags & fake_alt != fake_alt:
            event_type = KEYBOARD_EVENT_TYPES[w_param]
            is_extended = l_param.contents.flags & 1
            scan_code = l_param.contents.scan_code
            should_continue = process_key(event_type, virtual_key, scan_code, is_extended)
            if not should_continue:
                return -1

        return CallNextHookEx(None, n_code, w_param, l_param)

    keyboard_callback = LowLevelKeyboardProc(low_level_keyboard_handler)
    handle = ctypes.c_int(0)
    thread_id = wintypes.DWORD(0)
    SetWindowsHookEx(WH_KEYBOARD_LL, keyboard_callback, handle, thread_id)

    atexit.register(UnhookWindowsHookEx, keyboard_callback)

def listen(callback=no_function):
    '''Hook the keyboard'''
    _hooking_keyboard(callback)
    msg = LPMSG()
    while not GetMessage(msg, 0, 0, 0):
        TranslateMessage(msg)
        DispatchMessage(msg)

def do_inputs_respect_delay(filename):
    '''Get events from a file and replicate them, with delay.'''
    lt_event = _get_events_from_file(filename)
    for event in lt_event:
        if event.eventType == KEY_DOWN:
            press_key(event.vk)
        elif event.eventType == KEY_UP:
            release_key(event.vk)
        time.sleep(event.time)

def fast_inputs(filename):
    '''Get events from a file and replicate them, no delay.'''
    lt_event = _get_events_from_file(filename)
    for event in lt_event:
        if event.eventType == KEY_DOWN:
            press_key(event.vk)
        elif event.eventType == KEY_UP:
            release_key(event.vk)
