# Filename : functions.py
# Desc. : Contains all the function from the libs
#
# ----------------------------------------------------------------------------------#
import ctypes
from ctypes import wintypes

from structs import LPINPUT, MSLLHOOKSTRUCT, KBDLLHOOKSTRUCT, POINT, KeyboadStateType
from codes.KbdKeyName import vk_keys_name

user32 = ctypes.WinDLL('user32', use_last_error=True)
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

KeyboardState = KeyboadStateType()
nameBuffer = ctypes.create_unicode_buffer(32)
unicodeBuffer = ctypes.create_unicode_buffer(32)

if ctypes.sizeof(ctypes.c_long) == ctypes.sizeof(ctypes.c_void_p):
    WPARAM = ctypes.c_ulong
    LPARAM = ctypes.c_long
elif ctypes.sizeof(ctypes.c_longlong) == ctypes.sizeof(ctypes.c_void_p):
    WPARAM = ctypes.c_ulonglong
    LPARAM = ctypes.c_longlong


# ----------------------------------------------------------------------------------------------------------------------------
# For Windows focus
# ----------------------------------------------------------------------------------------------------------------------------
WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms633497(v=vs.85).aspx
EnumWindows = user32.EnumWindows
EnumWindows.argtypes = [WNDENUMPROC,wintypes.LPARAM]

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms633521(v=vs.85).aspx
GetWindowTextLengthW = user32.GetWindowTextLengthW
GetWindowTextLengthW.argtypes = [wintypes.HWND]

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms633520(v=vs.85).aspx
def GetWindowTextW(hwnd):
    length = GetWindowTextLengthW(hwnd) + 1
    buffer = ctypes.create_unicode_buffer(length)
    user32.GetWindowTextW(hwnd, buffer, length)
    return buffer.value

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms633553(v=vs.85).aspx
SetForegroundWindow = user32.SetForegroundWindow
SetForegroundWindow.argtypes = [wintypes.HWND]

# ----------------------------------------------------------------------------------------------------------------------------
# For input manipulation
# ----------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------
#https://msdn.microsoft.com/en-us/library/ms646290.aspx
# Needs to be launch with admin privileged (os.getuid() == 0)
BlockInput = user32.BlockInput
BlockInput.argtypes = [wintypes.BOOL]

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms683199(v=vs.85).aspx
GetModuleHandle = kernel32.GetModuleHandleW
GetModuleHandle.restype = wintypes.HMODULE
GetModuleHandle.argtypes = [wintypes.LPCWSTR]

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646301(v=vs.85).aspx
GetKeyState = user32.GetKeyState

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646299(v=vs.85).aspx
GetKeyboardState = user32.GetKeyboardState
GetKeyboardState.argtypes = [KeyboadStateType]
GetKeyboardState.restype = wintypes.BOOL

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646320(v=vs.85).aspx
ToUnicode = user32.ToUnicode
ToUnicode.argtypes = [ctypes.c_uint, ctypes.c_uint, KeyboadStateType, wintypes.LPWSTR, ctypes.c_int, ctypes.c_uint]
ToUnicode.restype = ctypes.c_int

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646300(v=vs.85).aspx
def GetKeyNameText(vk, scanCode, isExtented, modifiersState):
    KeyboardState[0x10] = 0x80 * modifiersState['SHIFT']
    KeyboardState[0x11] = 0x80 * modifiersState['ALTGR']
    KeyboardState[0x12] = 0x80 * modifiersState['ALTGR']
    KeyboardState[0x14] = 0x01 * modifiersState['NUMLOCK']
    KeyboardState[0x90] = 0x01 * modifiersState['CAPSLOCK']
    KeyboardState[0x91] = 0x01 * modifiersState['SCRLOCK']

    ret = ToUnicode(vk, scanCode, KeyboardState, unicodeBuffer, len(unicodeBuffer), 0)
    if ret and unicodeBuffer.value:
       yield unicodeBuffer.value
       # unicode_ret == -1 -> is dead key
       # ToUnicode has the side effect of setting global flags for dead keys.
       # Therefore we need to call it twice to clear those flags.
       # If your 6 and 7 keys are named "^6" and "^7", this is the reason.
       ToUnicode(vk, scanCode, KeyboardState, unicodeBuffer, len(unicodeBuffer), 0)

    ret = user32.GetKeyNameTextW(scanCode << 16 | isExtented << 24, nameBuffer, 1024)
    if ret and nameBuffer.value:
        yield nameBuffer.value
    if vk in vk_keys_name:
        yield vk_keys_name[vk]
    else:
        yield hex(vk)

# ----------------------------------------------------------------------------------------------------------------------------
# Get Cursor Position Function
# https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-getcursorpos
def GetCursorPos():
    point = POINT()
    user32.GetCursorPos(ctypes.byref(point))
    return point

# ----------------------------------------------------------------------------------------------------------------------------
# Mouse Cursor Move Function
# https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-setcursorpos
SetCursorPosFunc = user32.SetCursorPos

# ----------------------------------------------------------------------------------------------------------------------------
# Send Input Function (Mouse and Keyboard)
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646310%28v=vs.85%29.aspx
SendInputFunc = user32.SendInput
SendInputFunc.errcheck = _check_count
SendInputFunc.argtypes = (wintypes.UINT, LPINPUT, ctypes.c_int)

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646332(v=vs.85).aspx
user32.VkKeyScanExW.restype = wintypes.SHORT
def VkKeyScanEx(ch, hkl):
	res = user32.VkKeyScanExW(wintypes.WCHAR(ch), hkl)
	if res == -1:
		return -1, -1
	return res >> 8, res & 0xFF

# Not scan code, this is for VkKeyScanExW
SHIFT_KEY = 1
CTRL_KEY = 2
ALT_KEY = 4
HANKAKU_KEY = 8
RESERVED_KEY = [16,32] # Reserved (defined by the keyboard layout driver).
# ----------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------
# Hook functions
# ----------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------
LPMSG = ctypes.POINTER(wintypes.MSG)
LowLevelMouseProc = ctypes.CFUNCTYPE(ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM, ctypes.POINTER(MSLLHOOKSTRUCT))
LowLevelKeyboardProc = ctypes.CFUNCTYPE(ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM, ctypes.POINTER(KBDLLHOOKSTRUCT))

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms644990(v=vs.85).aspx
SetWindowsHookEx = user32.SetWindowsHookExA
SetWindowsHookEx.restype = wintypes.HHOOK

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/fr-fr/library/windows/desktop/ms644974(v=vs.85).aspx
CallNextHookEx = user32.CallNextHookEx
CallNextHookEx.restype = ctypes.c_int

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms644993(v=vs.85).aspx
UnhookWindowsHookEx = user32.UnhookWindowsHookEx
UnhookWindowsHookEx.argtypes = [wintypes.HHOOK]
UnhookWindowsHookEx.restype = wintypes.BOOL

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms644936(v=vs.85).aspx
GetMessage = user32.GetMessageW
GetMessage.argtypes = [LPMSG, ctypes.c_int, ctypes.c_int, ctypes.c_int]
GetMessage.restype = wintypes.BOOL

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms644955(v=vs.85).aspx
TranslateMessage = user32.TranslateMessage
TranslateMessage.argtypes = [LPMSG]
TranslateMessage.restype = wintypes.BOOL

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms644934(v=vs.85).aspx
DispatchMessage = user32.DispatchMessageA
DispatchMessage.argtypes = [LPMSG]
