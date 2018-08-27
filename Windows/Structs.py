'''
Structs definitions
'''
#pylint: disable=bad-whitespace
#pylint: disable=line-too-long
#pylint: disable=invalid-name
#pylint: disable=too-few-public-methods
#pylint: disable=missing-docstring

import ctypes
from ctypes import wintypes

from .codes.InputConst import MAPVK_VK_TO_VSC
from .codes.KbdScanCode import KEYEVENTF_UNICODE

_user32 = ctypes.WinDLL('user32', use_last_error=True)

KeyboadStateType = ctypes.c_uint8 * 256

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# Make the C struct definitions
wintypes.ULONG_PTR = wintypes.WPARAM

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms633519(v=vs.85).aspx
class RECT(ctypes.Structure):
    _fields_ = [("left",   wintypes.LONG),
                ("top",    wintypes.LONG),
                ("right",  wintypes.LONG),
                ("bottom", wintypes.LONG)]
    def __str__(self):
        return "left: " + str(self.left) + ",top: " +  str(self.top) + ",right: " + str(self.right) + ",bottom: " +  str(self.bottom)

# ----------------------------------------------------------------------------------------------------------------------------
class POINT(ctypes.Structure):
    _fields_ = [("X", wintypes.LONG),
                ("Y", wintypes.LONG)]

    def __sub__ (self, other):
        return POINT(other.X - self.X, other.Y - self.Y)
    def __str__(self):
        return "X: " + str(self.X) + ",Y: " +  str(self.Y)

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms632611(v=vs.85).aspx
class WINDOWPLACEMENT(ctypes.Structure):
    _fields_ = [("length"          , wintypes.UINT),
                ("flags"           , wintypes.UINT),
                ("showCmd"         , wintypes.UINT),
                ("ptMinPosition"   , POINT),
                ("ptMaxPosition"   , POINT),
                ("rcNormalPosition", RECT)]

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms644970(v=vs.85).aspx
class MSLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [("x",        wintypes.LONG),
                ("y",        wintypes.LONG),
                ("data",     ctypes.c_int32),
                ('reserved', ctypes.c_int32),
                ("flags",    wintypes.DWORD),
                ("time",     ctypes.c_int),]

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms644967(v=vs.85).aspx
class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [("vk_code",     wintypes.DWORD),
                ("scan_code",   wintypes.DWORD),
                ("flags",       wintypes.DWORD),
                ("time",        ctypes.c_int),
                ("dwExtraInfo", wintypes.ULONG_PTR)]

# ----------------------------------------------------------------------------------------------------------------------------
# https://docs.microsoft.com/fr-fr/windows/desktop/api/xinput/ns-xinput-_xinput_gamepad
class XINPUT_GAMEPAD(ctypes.Structure):
    _fields_ = [("wButtons"    , wintypes.WORD),
                ("bLeftTrigger", wintypes.BYTE),
                ("bLeftTrigger", wintypes.BYTE),
                ("sThumbLX"    , wintypes.SHORT),
                ("sThumbLY"    , wintypes.SHORT),
                ("sThumbRx"    , wintypes.SHORT),
                ("sThumbRy"    , wintypes.SHORT)]

# ----------------------------------------------------------------------------------------------------------------------------
# https://docs.microsoft.com/fr-fr/windows/desktop/api/xinput/ns-xinput-_xinput_state
class XINPUT_STATE(ctypes.Structure):
    _fields_ = [("dwPacketNumber", wintypes.DWORD),
                ("Gamepad", XINPUT_GAMEPAD)]

# ----------------------------------------------------------------------------------------------------------------------------
# https://docs.microsoft.com/fr-fr/windows/desktop/api/xinput/ns-xinput-_xinput_vibration
class XINPUT_VIBRATION(ctypes.Structure):
    _fields_ = [("wLeftMotorSpeed", wintypes.WORD),
                ("wRightMotorSpeed", wintypes.WORD)]

# ----------------------------------------------------------------------------------------------------------------------------
# https://docs.microsoft.com/fr-fr/windows/desktop/api/xinput/ns-xinput-_xinput_battery_information
class XINPUT_BATTERY_INFORMATION(ctypes.Structure):
    _fields_ = [("BatteryType", wintypes.BYTE),
                ("BatteryLevel", wintypes.BYTE)]

# ----------------------------------------------------------------------------------------------------------------------------
# https://docs.microsoft.com/fr-fr/windows/desktop/api/xinput/ns-xinput-_xinput_capabilities
class XINPUT_CAPABILITIES(ctypes.Structure):
    _fields_ = [("Type"     ,wintypes.BYTE),
                ("SubType"  ,wintypes.BYTE),
                ("Flags"    ,wintypes.WORD),
                ("Gamepad"  ,XINPUT_GAMEPAD),
                ("Vibration",XINPUT_VIBRATION)]

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
    _fields_ = [("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR)]

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = _user32.MapVirtualKeyExW(self.wVk, MAPVK_VK_TO_VSC, 0)

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646269(v=vs.85).aspx
class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD)]

# ----------------------------------------------------------------------------------------------------------------------------
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646270(v=vs.85).aspx
class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT)]
    _anonymous_ = ("_input",)
    _fields_    = [("type",   wintypes.DWORD),
                   ("_input", _INPUT)]


LPINPUT = ctypes.POINTER(INPUT)
