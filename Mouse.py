import time
import ctypes
import atexit

from structs   import POINT, INPUT, MOUSEINPUT
from functions import (user32, LowLevelMouseProc, GetCursorPos, SetCursorPosFunc, SendInputFunc, 
                       SetWindowsHookEx, CallNextHookEx, UnhookWindowsHookEx, GetMessage, TranslateMessage, 
                       DispatchMessage, LPMSG)
from codes.MouseScanCode import *
from codes.InputConst import *
from mouseEvent import *

OUTPUT_FILENAME = "mouseInputs.yapam"

NULL = ctypes.c_int(0)

calcDelta = lambda delta : delta / (WHEEL_DELTA * (2<<15))
sendLamb = lambda x : SendInputFunc(1, ctypes.byref(x), ctypes.sizeof(x))

def noFunction(event):
    return None

def writeToFileEvents(event):
    with open(OUTPUT_FILENAME, "a") as f:
        f.write(str(event) + "\n")

class Mouse():
    def __MouseButtonDown(self, side):
        x = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(dwFlags=inputMouseButton[DOWN][side]))
        sendLamb(x)
    
    def __MouseButtonUp(self, side):
        x = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(dwFlags=inputMouseButton[UP][side]))
        sendLamb(x)
    
    def __sendCode(self, code):
        x = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(dwFlags=code))
        sendLamb(x)
    
    # Seems to not work as intended
    def MoveRelative(self, x, y):
        x = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(dx=int(x), dy=int(y), dwFlags=MOUSEEVENTF_MOVE))
        sendLamb(x)

    # Move upwards if delta > 0
    def MoveWheel(self, delta=1):
        x = INPUT(type=INPUT_MOUSE,mi=MOUSEINPUT(mouseData=int(delta * WHEEL_DELTA), dwFlags=inputMouseButton[WHEEL][VERTICAL]))
        sendLamb(x)

    def GetPosition(self):
        return GetCursorPos()

    def MoveTo(self, x, y):
        SetCursorPosFunc(int(x), int(y))

    def Click(self, side):
        self.__MouseButtonDown(side)
        self.__MouseButtonUp(side)

    def HookMouse(self, callback=noFunction):
        def low_level_mouse_handler(nCode, wParam, lParam):

            struct = lParam.contents
            t = time.time()

            # Determine what type of event it is
            if wParam == WM_MOUSEMOVE:
                event = MoveEvent(struct.x, struct.y, t)
            elif wParam == WM_MOUSEWHEEL:
                event = WheelEvent(calcDelta(struct.data), t)
            elif wParam in wmCodeButton:
                event = ButtonEvent(wParam, struct.data, t)

            callback(event)
            return CallNextHookEx(NULL, nCode, wParam, lParam)

        mouseCallback = LowLevelMouseProc(low_level_mouse_handler)
        mouseHook = SetWindowsHookEx(WH_MOUSE_LL, mouseCallback, NULL, NULL)
        atexit.register(UnhookWindowsHookEx, mouseHook)

        msg = LPMSG()
        while not GetMessage(msg, NULL, NULL, NULL):
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
            if isinstance(event, MoveEvent):
                self.MoveTo(event.X, event.Y)
            elif isinstance(event, WheelEvent):
                self.MoveWheel(event.delta)
            elif isinstance(event, ButtonEvent):
                self.__sendCode(event.code)
            time.sleep(event.time)
    
    def FastInputs(self, filename):
        lt = self.__GetEventsFromFile(filename)
        for event in lt:
            if isinstance(event, MoveEvent):
                self.MoveTo(event.X, event.Y)
            elif isinstance(event, WheelEvent):
                self.MoveWheel(event.delta)
            elif isinstance(event, ButtonEvent):
                self.__sendCode(event.code)
            

if __name__ == "__main__":
    m = Mouse()
    #m.HookMouse(writeToFileEvents)
    #m.DoInputsRespectDelay(OUTPUT_FILENAME)
    #m.FastInputs(OUTPUT_FILENAME)