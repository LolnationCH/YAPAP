'''
Mouse interface
'''
#pylint: disable=unused-wildcard-import
#pylint: disable=wildcard-import
#pylint: disable=invalid-name
#pylint: disable=unused-import
import time
import ctypes
import atexit

from .Structs   import INPUT, MOUSEINPUT
from .Functions import (LowLevelMouseProc, GetCursorPos, SetCursorPosFunc, SendInputFunc,
                        SetWindowsHookEx, CallNextHookEx, UnhookWindowsHookEx, GetMessage,
                        TranslateMessage, DispatchMessage, LPMSG)
from .codes.MouseScanCode import *
from .codes.InputConst import *
from .MouseEvent import *

OUTPUT_FILENAME = "mouseInputs.yapam"

NULL = ctypes.c_int(0)

CALC_DELTA = lambda delta: delta / (WHEEL_DELTA * (2<<15))
SEND_INPUT = lambda x: SendInputFunc(1, ctypes.byref(x), ctypes.sizeof(x))

def noFunction(_):
    '''.'''
    return None

# This is more of an example, since you cannot change the value of OUTPUT_FILENAME
def writeToFileEvents(event):
    '''Basic write the event to file function, can be passed to the listen function.'''
    with open(OUTPUT_FILENAME, "a") as f:
        f.write(str(event) + "\n")

def __GetEventsFromFile(filename):
    '''Get a list of the events contain in a file.'''
    with open(filename) as f:
        data = f.read().split('\n')

    lt = []
    last_time = parse_event(data[0], 0)[1]
    for x in data:
        if x == '':
            continue
        event, last_time = parse_event(x, last_time)
        if event is not None:
            lt.append(event)
        else:
            print("Line not formated correctly : {}")
    return lt

def __MouseButtonDown(side):
    '''Send a DOWn event with a specify "side" of the mouse.'''
    SEND_INPUT(INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(dwFlags=INPUT_MOUSE_BOUTTON[DOWN][side])))

def __MouseButtonUp(side):
    '''Send a UP event with a specify "side" of the mouse.'''
    SEND_INPUT(INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(dwFlags=INPUT_MOUSE_BOUTTON[UP][side])))

def __sendCode(code):
    '''Send the code, can be a UP or DOWN event.'''
    SEND_INPUT(INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(dwFlags=code)))

# Seems to not work as intended TODO
def MoveRelative(x, y):
    '''Move relative to the current position of the mouse.'''
    SEND_INPUT(INPUT(type=INPUT_MOUSE,
                     mi=MOUSEINPUT(dx=int(x), dy=int(y), dwFlags=MOUSEEVENTF_MOVE)))

# Move upwards if delta > 0
def MoveWheel(delta=1):
    '''Move the wheel times the delta. If delta < 0, then move upwards'''
    SEND_INPUT(INPUT(type=INPUT_MOUSE,
                     mi=MOUSEINPUT(mouseData=int(delta * WHEEL_DELTA),
                                   dwFlags=INPUT_MOUSE_BOUTTON[WHEEL][VERTICAL])))

def MoveTo(x, y):
    '''Move the cursor to the specify position.'''
    SetCursorPosFunc(int(x), int(y))

def Click(side):
    '''Simulate a click of the specify button.'''
    __MouseButtonDown(side)
    __MouseButtonUp(side)

def _hookingMouse(callback):
    '''Hooking function of the moouse.'''
    def low_level_mouse_handler(nCode, wParam, lParam):

        struct = lParam.contents
        t = time.time()

        # Determine what type of event it is
        if wParam == WM_MOUSEMOVE:
            event = MoveEvent(struct.x, struct.y, t)
        elif wParam == WM_MOUSEWHEEL:
            event = WheelEvent(CALC_DELTA(struct.data), t)
        elif wParam in WM_CODE_BUTTON:
            event = ButtonEvent(wParam, struct.data, t)

        callback(event)
        return CallNextHookEx(NULL, nCode, wParam, lParam)

    mouseCallback = LowLevelMouseProc(low_level_mouse_handler)
    mouseHook = SetWindowsHookEx(WH_MOUSE_LL, mouseCallback, NULL, NULL)
    atexit.register(UnhookWindowsHookEx, mouseHook)

def Listen(callback=noFunction):
    '''Hook the mouse.'''
    _hookingMouse(callback)
    msg = LPMSG()
    while not GetMessage(msg, NULL, NULL, NULL):
        TranslateMessage(msg)
        DispatchMessage(msg)

def DoInputsRespectDelay(filename):
    '''Get events from a file and replicate them, with delay.'''
    lt = __GetEventsFromFile(filename)
    for event in lt:
        if isinstance(event, MoveEvent):
            MoveTo(event.X, event.Y)
        elif isinstance(event, WheelEvent):
            MoveWheel(event.delta)
        elif isinstance(event, ButtonEvent):
            __sendCode(event.code)
        time.sleep(event.time)

def FastInputs(filename):
    '''Get events from a file and replicate them, no delay.'''
    lt = __GetEventsFromFile(filename)
    for event in lt:
        if isinstance(event, MoveEvent):
            MoveTo(event.X, event.Y)
        elif isinstance(event, WheelEvent):
            MoveWheel(event.delta)
        elif isinstance(event, ButtonEvent):
            __sendCode(event.code)
