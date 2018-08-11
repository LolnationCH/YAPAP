# Filename : Winuser.py
# Desc. : Make Winuser.h to python
#
# ----------------------------------------------------------------------------------#
import ctypes
from ctypes import wintypes

from codes.InputConst import *
from codes.KbdScanCode import KEYEVENTF_UNICODE

user32 = ctypes.WinDLL('user32', use_last_error=True)
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# https://msdn.microsoft.com/en-us/library/windows/desktop/ms683199(v=vs.85).aspx
kernel32.GetModuleHandleW.restype = wintypes.HMODULE
kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# Make the C struct definitions
wintypes.ULONG_PTR = wintypes.WPARAM

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms644970(v=vs.85).aspx
class MSLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long),
                ('data', ctypes.c_int32),
                ('reserved', ctypes.c_int32),
                ("flags", wintypes.DWORD),
                ("time", ctypes.c_int),
                ]


# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms644967(v=vs.85).aspx
class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [("vk_code",     wintypes.DWORD),
                ("scan_code",   wintypes.DWORD),
                ("flags",       wintypes.DWORD),
                ("time",        ctypes.c_int),
                ("dwExtraInfo", wintypes.ULONG_PTR)]


# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646273(v=vs.85).aspx
class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646271(v=vs.85).aspx
class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk, MAPVK_VK_TO_VSC, 0)

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646269(v=vs.85).aspx
class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646270(v=vs.85).aspx
class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_    = (("type",   wintypes.DWORD),
                   ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# Mouse Cursor Move Function
# https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-setcursorpos
SetCursorPosFunc = ctypes.windll.user32.SetCursorPos

# Send Input Function (Mouse and Keyboard)
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646310%28v=vs.85%29.aspx
SendInputFunc = ctypes.windll.user32.SendInput

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args
SendInputFunc.errcheck = _check_count
SendInputFunc.argtypes = (wintypes.UINT, # nInputs
                          LPINPUT,       # pInputs
                          ctypes.c_int)  # cbSize


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