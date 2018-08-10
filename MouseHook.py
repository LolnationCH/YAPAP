# FILE TO BE DELETED

import ctypes
import time
import atexit

from mouseEvent import *
from codes.MouseScanCode import *
from structs import POINT
from functions import (user32, LowLevelMouseProc, SetWindowsHookEx, CallNextHookEx, UnhookWindowsHookEx,
                       GetMessage, TranslateMessage, DispatchMessage, LPMSG)

NULL = ctypes.c_int(0)

def listen(callback):
    def low_level_mouse_handler(nCode, wParam, lParam):
        struct = lParam.contents
        # struct.time is most of the time zero.
        t = time.time()

        if wParam == WM_MOUSEMOVE:
            event = MoveEvent(struct.x, struct.y, t)
        elif wParam == WM_MOUSEWHEEL:
            event = WheelEvent(struct.data / (WHEEL_DELTA * (2<<15)), t)
        elif wParam in wmCodeButton:
            type, button = wmCodeButton.get(wParam, ('?', '?'))
            if wParam >= WM_XBUTTONDOWN:
                button = wParam[struct.data]
            event = ButtonEvent(type, button, t, wParam)

        callback(event)
        return CallNextHookEx(NULL, nCode, wParam, lParam)

    WH_MOUSE_LL = ctypes.c_int(14)
    mouse_callback = LowLevelMouseProc(low_level_mouse_handler)
    mouse_hook = SetWindowsHookEx(WH_MOUSE_LL, mouse_callback, NULL, NULL)

    # Register to remove the hook when the interpreter exits. Unfortunately a
    # try/finally block doesn't seem to work here.
    atexit.register(UnhookWindowsHookEx, mouse_hook)

    msg = LPMSG()
    while not GetMessage(msg, NULL, NULL, NULL):
        TranslateMessage(msg)
        DispatchMessage(msg)

if __name__ == '__main__':
    listen(print)