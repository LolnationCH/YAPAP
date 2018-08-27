'''
Theses are all the scancodes for a keyboard and their function that I could find.
'''
# pylint: disable=bad-whitespace
# pylint: disable=line-too-long

#-------------------------------   REFERENCE ---------------------------------------#
#
# msdn.microsoft.com/en-us/library/dd375731
# https://docs.microsoft.com/fr-fr/windows/desktop/inputdev/virtual-key-codes
# ----------------------------------------------------------------------------------#
#
# KEYBDINPUT structure
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646271(v=vs.85).aspx
# ----------------------------------------------------------------------------------#
#
# winuser.h
# C:\Program Files (x86)\Microsoft SDKs\Windows\vX.Xx\Include\WinUser.h
# ----------------------------------------------------------------------------------#
#
# KeyboardEvent.Keycode
# https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/keyCode
# ----------------------------------------------------------------------------------#
# Note :
# _WIN32_WINNT Values :
# Windows 8.1	                                            _WIN32_WINNT_WINBLUE (0x0602)
# Windows 8	                                                _WIN32_WINNT_WIN8 (0x0602)
# Windows 7	                                                _WIN32_WINNT_WIN7 (0x0601)
# Windows Server 2008	                                    _WIN32_WINNT_WS08 (0x0600)
# Windows Vista	                                            _WIN32_WINNT_VISTA (0x0600)
# Windows Server 2003 with SP1, Windows XP with SP2	        _WIN32_WINNT_WS03 (0x0502)
# Windows Server 2003, Windows XP	                        _WIN32_WINNT_WINXP (0x0501)
# PS. So basically about almost every Windows currently running have all these codes
# ----------------------------------------------------------------------------------#

# dwFlags for KEYBDINPUT
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646271(v=vs.85).aspx
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008
#-----------------------------------------------------------------------------------#

WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_SYSKEYDOWN = 0x104 # Used for ALT key
WM_SYSKEYUP = 0x105

# Mouse buttons (Not sure what they are used for since this is for keyboard)
VK_LBUTTON  = 0x01 # Left mouse button
VK_RBUTTON  = 0x02 # Right mouse button
VK_CANCEL   = 0x03 # Control-break processing (Ctrl-c most of the time)
VK_MBUTTON  = 0x04 # Middle mouse button (three-button mouse) NOT contiguous with L & RBUTTON
# if _WIN32_WINNT >= 0x0500
VK_XBUTTON1 = 0x05 # X1 mouse button. NOT contiguous with L & RBUTTON
VK_XBUTTON2 = 0x06 # X2 mouse button. NOT contiguous with L & RBUTTON
#-----------------------------------------------------------------------------------#

# Frequently Used Keys and others
VK_BACK       = 0x08 # BACKSPACE key
VK_TAB        = 0x09 # TAB key
VK_CLEAR      = 0x0C # CLEAR key
VK_RETURN     = 0x0D # ENTER key
VK_SHIFT      = 0x10 # SHIFT key
VK_CONTROL    = 0x11 # CTRL key
VK_MENU       = 0x12 # ALT key
VK_PAUSE      = 0x13 # PAUSE key
VK_CAPITAL    = 0x14 # CAPS LOCK key
VK_KANA       = 0x15 # IME Kana mode
VK_HANGUEL    = 0x15 # IME Hanguel mode (maintained for compatibility; use VK_HANGUL)
VK_HANGUL     = 0x15 # IME Hangul mode
VK_JUNJA      = 0x17 # IME Junja mode
VK_FINAL      = 0x18 # IME final mode
VK_HANJA      = 0x19 # IME Hanja mode
VK_KANJI      = 0x19 # IME Kanji mode
VK_ESCAPE     = 0x1B # ESC key
VK_CONVERT    = 0x1C # IME convert
VK_NONCONVERT = 0x1D # IME nonconvert
VK_ACCEPT     = 0x1E # IME accept
VK_MODECHANGE = 0x1F # IME mode change request
VK_SPACE      = 0x20 # SPACEBAR
VK_PRIOR      = 0x21 # PAGE UP key
VK_NEXT       = 0x22 # PAGE DOWN key
VK_END        = 0x23 # END key
VK_HOME       = 0x24 # HOME key
VK_LEFT       = 0x25 # LEFT ARROW key
VK_UP         = 0x26 # UP ARROW key
VK_RIGHT      = 0x27 # RIGHT ARROW key
VK_DOWN       = 0x28 # DOWN ARROW key
VK_SELECT     = 0x29 # SELECT key
VK_PRINT      = 0x2A # PRINT key
VK_EXECUTE    = 0x2B # EXECUTE key
VK_SNAPSHOT   = 0x2C # PRINT SCREEN key
VK_INSERT     = 0x2D # INS key
VK_DELETE     = 0x2E # DEL key
VK_HELP       = 0x2F # HELP key
#-----------------------------------------------------------------------------------#

# AlphaNumeric
VK_KEY_0 = 0x30 # 0 key
VK_KEY_1 = 0x31 # 1 key
VK_KEY_2 = 0x32 # 2 key
VK_KEY_3 = 0x33 # 3 key
VK_KEY_4 = 0x34 # 4 key
VK_KEY_5 = 0x35 # 5 key
VK_KEY_6 = 0x36 # 6 key
VK_KEY_7 = 0x37 # 7 key
VK_KEY_8 = 0x38 # 8 key
VK_KEY_9 = 0x39 # 9 key

VK_KEY_A = 0x41 # A key
VK_KEY_B = 0x42 # B key
VK_KEY_C = 0x43 # C key
VK_KEY_D = 0x44 # D key
VK_KEY_E = 0x45 # E key
VK_KEY_F = 0x46 # F key
VK_KEY_G = 0x47 # G key
VK_KEY_H = 0x48 # H key
VK_KEY_I = 0x49 # I key
VK_KEY_J = 0x4A # J key
VK_KEY_K = 0x4B # K key
VK_KEY_L = 0x4C # L key
VK_KEY_M = 0x4D # M key
VK_KEY_N = 0x4E # N key
VK_KEY_O = 0x4F # O key
VK_KEY_P = 0x50 # P key
VK_KEY_Q = 0x51 # Q key
VK_KEY_R = 0x52 # R key
VK_KEY_S = 0x53 # S key
VK_KEY_T = 0x54 # T key
VK_KEY_U = 0x55 # U key
VK_KEY_V = 0x56 # V key
VK_KEY_W = 0x57 # W key
VK_KEY_X = 0x58 # X key
VK_KEY_Y = 0x59 # Y key
VK_KEY_Z = 0x5A # Z key
#-----------------------------------------------------------------------------------#

VK_LWIN      = 0x5B # Left Windows key (Natural keyboard)
VK_RWIN      = 0x5C # Right Windows key (Natural keyboard)
VK_APPS      = 0x5D # Applications key (Natural keyboard)
VK_SLEEP     = 0x5F # Computer Sleep key

# NUMPAD
VK_NUMPAD0   = 0x60 # Numeric keypad 0 key
VK_NUMPAD1   = 0x61 # Numeric keypad 1 key
VK_NUMPAD2   = 0x62 # Numeric keypad 2 key
VK_NUMPAD3   = 0x63 # Numeric keypad 3 key
VK_NUMPAD4   = 0x64 # Numeric keypad 4 key
VK_NUMPAD5   = 0x65 # Numeric keypad 5 key
VK_NUMPAD6   = 0x66 # Numeric keypad 6 key
VK_NUMPAD7   = 0x67 # Numeric keypad 7 key
VK_NUMPAD8   = 0x68 # Numeric keypad 8 key
VK_NUMPAD9   = 0x69 # Numeric keypad 9 key
VK_MULTIPLY  = 0x6A # Multiply key
VK_ADD       = 0x6B # Add key
VK_SEPARATOR = 0x6C # Separator key
VK_SUBTRACT  = 0x6D # Subtract key
VK_DECIMAL   = 0x6E # Decimal key
VK_DIVIDE    = 0x6F # Divide key
#-----------------------------------------------------------------------------------#

# F# Keys
VK_F1  = 0x70 # F1 key
VK_F2  = 0x71 # F2 key
VK_F3  = 0x72 # F3 key
VK_F4  = 0x73 # F4 key
VK_F5  = 0x74 # F5 key
VK_F6  = 0x75 # F6 key
VK_F7  = 0x76 # F7 key
VK_F8  = 0x77 # F8 key
VK_F9  = 0x78 # F9 key
VK_F10 = 0x79 # F10 key
VK_F11 = 0x7A # F11 key
VK_F12 = 0x7B # F12 key
VK_F13 = 0x7C # F13 key
VK_F14 = 0x7D # F14 key
VK_F15 = 0x7E # F15 key
VK_F16 = 0x7F # F16 key
VK_F17 = 0x80 # F17 key
VK_F18 = 0x81 # F18 key
VK_F19 = 0x82 # F19 key
VK_F20 = 0x83 # F20 key
VK_F21 = 0x84 # F21 key
VK_F22 = 0x85 # F22 key
VK_F23 = 0x86 # F23 key
VK_F24 = 0x87 # F24 key
#-----------------------------------------------------------------------------------#

# Functionalities Keys
VK_NUMLOCK  = 0x90 # NUM LOCK key
VK_SCROLL   = 0x91 # SCROLL LOCK key
VK_LSHIFT   = 0xA0 # Left SHIFT key
VK_RSHIFT   = 0xA1 # Right SHIFT key
VK_LCONTROL = 0xA2 # Left CONTROL key
VK_RCONTROL = 0xA3 # Right CONTROL key
VK_LMENU    = 0xA4 # Left MENU key
VK_RMENU    = 0xA5 # Right MENU key
#-----------------------------------------------------------------------------------#

#  NEC PC-9800 kbd definitions and Fujitsu/OASYS kbd definitions
VK_OEM_NEC_EQUAL  = 0x92   # '=' key on numpad SPECIFIC ONLY TO NEC PC-9800 kbd definitions
VK_OEM_FJ_JISHO   = 0x92   # 'Dictionary' key. SPECIFIC ONLY Fujitsu/OASYS kbd definitions
VK_OEM_FJ_MASSHOU = 0x93   # 'Unregister word' key. SPECIFIC ONLY Fujitsu/OASYS kbd definitions
VK_OEM_FJ_TOUROKU = 0x94   # 'Register word' key. SPECIFIC ONLY Fujitsu/OASYS kbd definitions
VK_OEM_FJ_LOYA    = 0x95   # 'Left OYAYUBI' key. SPECIFIC ONLY Fujitsu/OASYS kbd definitions
VK_OEM_FJ_ROYA    = 0x96   # 'Right OYAYUBI' key. SPECIFIC ONLY Fujitsu/OASYS kbd definitions
#-----------------------------------------------------------------------------------#

# Media Keys if _WIN32_WINNT >= 0x0500
VK_BROWSER_BACK        = 0xA6 # Browser Back key
VK_BROWSER_FORWARD     = 0xA7 # Browser Forward key
VK_BROWSER_REFRESH     = 0xA8 # Browser Refresh key
VK_BROWSER_STOP        = 0xA9 # Browser Stop key
VK_BROWSER_SEARCH      = 0xAA # Browser Search key
VK_BROWSER_FAVORITES   = 0xAB # Browser Favorites key
VK_BROWSER_HOME        = 0xAC # Browser Start and Home key
VK_VOLUME_MUTE         = 0xAD # Volume Mute key
VK_VOLUME_DOWN         = 0xAE # Volume Down key
VK_VOLUME_UP           = 0xAF # Volume Up key
VK_MEDIA_NEXT_TRACK    = 0xB0 # Next Track key
VK_MEDIA_PREV_TRACK    = 0xB1 # Previous Track key
VK_MEDIA_STOP          = 0xB2 # Stop Media key
VK_MEDIA_PLAY_PAUSE    = 0xB3 # Play/Pause Media key
VK_LAUNCH_MAIL         = 0xB4 # Start Mail key
VK_LAUNCH_MEDIA_SELECT = 0xB5 # Select Media key
VK_LAUNCH_APP1         = 0xB6 # Start Application 1 key
VK_LAUNCH_APP2         = 0xB7 # Start Application 2 key
#-----------------------------------------------------------------------------------#

# OEM Keys and extra
VK_OEM_1      = 0xBA # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard the ';=' key
VK_OEM_PLUS   = 0xBB # For any country/region the '+' key
VK_OEM_COMMA  = 0xBC # For any country/region the '' key
VK_OEM_MINUS  = 0xBD # For any country/region the '-' key
VK_OEM_PERIOD = 0xBE # For any country/region the '.' key
VK_OEM_2      = 0xBF # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard the '/?' key
VK_OEM_3      = 0xC0 # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard the '`~' key
VK_OEM_4      = 0xDB # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard the '[{' key
VK_OEM_5      = 0xDC # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard the '\|' key
VK_OEM_6      = 0xDD # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard the ']}' key
VK_OEM_7      = 0xDE # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard the ''"' key
VK_OEM_8      = 0xDF # Used for miscellaneous characters; it can vary by keyboard.
VK_OEM_AX     = 0xE1  # 'AX' key on Japanese AX kbd
VK_OEM_102    = 0xE2  # "<>" or "\|" on RT 102-key kbd.
VK_ICO_HELP   = 0xE3  # Help key on ICO. This is (was?) used for Olivetti ICO keyboard.
VK_ICO_00     = 0xE4  # 00 key on ICO. This is (was?) used for Olivetti ICO keyboard.
VK_PROCESSKEY = 0xE5 # IME PROCESS key
VK_ICO_CLEAR  = 0xE6 # An OEM specific key on Windows. This is (was?) used for Olivetti ICO keyboard.
VK_PACKET     = 0xE7 # Used to pass Unicode characters as if they were keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information see Remark in KEYBDINPUT SendInput WM_KEYDOWN and WM_KEYUP
VK_ATTN       = 0xF6 # Attn (Attention) key of IBM midrange computers e.g. AS/400.
VK_CRSEL      = 0xF7 # CrSel (Cursor Selection) key of IBM 3270 keyboard layout.
VK_EXSEL      = 0xF8 # ExSel (Extend Selection) key of IBM 3270 keyboard layout.
VK_EREOF      = 0xF9 # Erase EOF key of IBM 3270 keyboard layout.
VK_PLAY       = 0xFA # Play key of IBM 3270 keyboard layout.
VK_ZOOM       = 0xFB # Zoom key
VK_PA1        = 0xFD # PA1 key
VK_OEM_CLEAR  = 0xFE # Clear key
#-----------------------------------------------------------------------------------#

# Nokia/Ericsson definitions
VK_OEM_RESET   = 0xE9
VK_OEM_JUMP    = 0xEA
VK_OEM_PA1     = 0xEB
VK_OEM_PA2     = 0xEC
VK_OEM_PA3     = 0xED
VK_OEM_WSCTRL  = 0xEE
VK_OEM_CUSEL   = 0xEF
VK_OEM_ATTN    = 0xF0
VK_OEM_FINISH  = 0xF1
VK_OEM_COPY    = 0xF2
VK_OEM_AUTO    = 0xF3
VK_OEM_ENLW    = 0xF4
VK_OEM_BACKTAB = 0xF5
VK_ATTN        = 0xF6
VK_CRSEL       = 0xF7
VK_EXSEL       = 0xF8
VK_EREOF       = 0xF9
VK_PLAY        = 0xFA
VK_ZOOM        = 0xFB
VK_NONAME      = 0xFC
VK_PA1         = 0xFD
VK_OEM_CLEAR   = 0xFE
#-----------------------------------------------------------------------------------#

LT_NUMPAD = [
    VK_NUMPAD0,
    VK_NUMPAD1,
    VK_NUMPAD2,
    VK_NUMPAD3,
    VK_NUMPAD4,
    VK_NUMPAD5,
    VK_NUMPAD6,
    VK_NUMPAD7,
    VK_NUMPAD8,
    VK_NUMPAD9,
    VK_MULTIPLY,
    VK_ADD,
    VK_SEPARATOR,
    VK_SUBTRACT,
    VK_DECIMAL,
    VK_DIVIDE
]

# https://github.com/boppreh/keyboard/blob/master/keyboard/_winkeyboard.py
LT_OTHER_NUMPAD = [
    (126, 194, 0),
    (126, 194, 0),
    (28, 13, 1),
    (28, 13, 1),
    (69, 144, 1),
    (69, 144, 1),
    (71, 36, 0),
    (72, 38, 0),
    (73, 33, 0),
    (75, 37, 0),
    (76, 12, 0),
    (77, 39, 0),
    (79, 35, 0),
    (80, 40, 0),
    (81, 34, 0),
    (82, 45, 0),
    (83, 46, 0)
]
#-----------------------------------------------------------------------------------#

# Undefined, Reserved and OEM specific
_ = 0x07 # Undefined
_ = [0x0A, 0x0B] # Reserved
_ = [0x0E, 0x0F] # Undefined
_ = 0x16 # Undefined
_ = 0x1A # Undefined
_ = [0x3A, 0x40] # Undefined
_ = 0x5E # Reserved
_ = [0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8D, 0x8F] # Unassigned
_ = [0x97,0x98, 0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E, 0x9F] # Unassigned
_ = [0xB8, 0xB9] # Reserved
_ = [0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xca, 0xcb, 0xcc, 0xcd, 0xce, 0xcf, 0xd0, 0xd1, 0xd2, 0xd3, 0xd4, 0xd5, 0xd6, 0xD7] # Reserved
_ = [0xD8, 0xD9, 0xDA] # Unassigned
_ = 0xE0 # Reserved
_ = 0xE8 # Unassigned
_ = [0xE9, 0xEA, 0xEB, 0xEC, 0xED, 0xEE, 0xEF, 0xF0, 0xF1, 0xF2, 0xF3, 0xF4] # OEM specific
VK_NONAME = 0xFC # Reserved


VK_KEYS_NAME = {
    VK_LBUTTON : "VK_LBUTTON",
    VK_RBUTTON : "VK_RBUTTON",
    VK_CANCEL : "VK_CANCEL",
    VK_MBUTTON : "VK_MBUTTON",
    VK_XBUTTON1 : "VK_XBUTTON1",
    VK_XBUTTON2 : "VK_XBUTTON2",
    VK_BACK : "VK_BACK",
    VK_TAB : "VK_TAB",
    VK_CLEAR : "VK_CLEAR",
    VK_RETURN : "VK_RETURN",
    VK_SHIFT : "VK_SHIFT",
    VK_CONTROL : "VK_CONTROL",
    VK_MENU : "VK_MENU",
    VK_PAUSE : "VK_PAUSE",
    VK_CAPITAL : "VK_CAPITAL",
    VK_KANA : "VK_KANA",
    VK_HANGUEL : "VK_HANGUEL",
    VK_HANGUL : "VK_HANGUL",
    VK_JUNJA : "VK_JUNJA",
    VK_FINAL : "VK_FINAL",
    VK_HANJA : "VK_HANJA",
    VK_KANJI : "VK_KANJI",
    VK_ESCAPE : "VK_ESCAPE",
    VK_CONVERT : "VK_CONVERT",
    VK_NONCONVERT : "VK_NONCONVERT",
    VK_ACCEPT : "VK_ACCEPT",
    VK_MODECHANGE : "VK_MODECHANGE",
    VK_SPACE : "VK_SPACE",
    VK_PRIOR : "VK_PRIOR",
    VK_NEXT : "VK_NEXT",
    VK_END : "VK_END",
    VK_HOME : "VK_HOME",
    VK_LEFT : "VK_LEFT",
    VK_UP : "VK_UP",
    VK_RIGHT : "VK_RIGHT",
    VK_DOWN : "VK_DOWN",
    VK_SELECT : "VK_SELECT",
    VK_PRINT : "VK_PRINT",
    VK_EXECUTE : "VK_EXECUTE",
    VK_SNAPSHOT : "VK_SNAPSHOT",
    VK_INSERT : "VK_INSERT",
    VK_DELETE : "VK_DELETE",
    VK_HELP : "VK_HELP",
    VK_KEY_0 : "VK_KEY_0",
    VK_KEY_1 : "VK_KEY_1",
    VK_KEY_2 : "VK_KEY_2",
    VK_KEY_3 : "VK_KEY_3",
    VK_KEY_4 : "VK_KEY_4",
    VK_KEY_5 : "VK_KEY_5",
    VK_KEY_6 : "VK_KEY_6",
    VK_KEY_7 : "VK_KEY_7",
    VK_KEY_8 : "VK_KEY_8",
    VK_KEY_9 : "VK_KEY_9",
    VK_KEY_A : "VK_KEY_A",
    VK_KEY_B : "VK_KEY_B",
    VK_KEY_C : "VK_KEY_C",
    VK_KEY_D : "VK_KEY_D",
    VK_KEY_E : "VK_KEY_E",
    VK_KEY_F : "VK_KEY_F",
    VK_KEY_G : "VK_KEY_G",
    VK_KEY_H : "VK_KEY_H",
    VK_KEY_I : "VK_KEY_I",
    VK_KEY_J : "VK_KEY_J",
    VK_KEY_K : "VK_KEY_K",
    VK_KEY_L : "VK_KEY_L",
    VK_KEY_M : "VK_KEY_M",
    VK_KEY_N : "VK_KEY_N",
    VK_KEY_O : "VK_KEY_O",
    VK_KEY_P : "VK_KEY_P",
    VK_KEY_Q : "VK_KEY_Q",
    VK_KEY_R : "VK_KEY_R",
    VK_KEY_S : "VK_KEY_S",
    VK_KEY_T : "VK_KEY_T",
    VK_KEY_U : "VK_KEY_U",
    VK_KEY_V : "VK_KEY_V",
    VK_KEY_W : "VK_KEY_W",
    VK_KEY_X : "VK_KEY_X",
    VK_KEY_Y : "VK_KEY_Y",
    VK_KEY_Z : "VK_KEY_Z",
    VK_LWIN : "VK_LWIN",
    VK_RWIN : "VK_RWIN",
    VK_APPS : "VK_APPS",
    VK_SLEEP : "VK_SLEEP",
    VK_NUMPAD0 : "VK_NUMPAD0",
    VK_NUMPAD1 : "VK_NUMPAD1",
    VK_NUMPAD2 : "VK_NUMPAD2",
    VK_NUMPAD3 : "VK_NUMPAD3",
    VK_NUMPAD4 : "VK_NUMPAD4",
    VK_NUMPAD5 : "VK_NUMPAD5",
    VK_NUMPAD6 : "VK_NUMPAD6",
    VK_NUMPAD7 : "VK_NUMPAD7",
    VK_NUMPAD8 : "VK_NUMPAD8",
    VK_NUMPAD9 : "VK_NUMPAD9",
    VK_MULTIPLY : "VK_MULTIPLY",
    VK_ADD : "VK_ADD",
    VK_SEPARATOR : "VK_SEPARATOR",
    VK_SUBTRACT : "VK_SUBTRACT",
    VK_DECIMAL : "VK_DECIMAL",
    VK_DIVIDE : "VK_DIVIDE",
    VK_F1 : "VK_F1",
    VK_F2 : "VK_F2",
    VK_F3 : "VK_F3",
    VK_F4 : "VK_F4",
    VK_F5 : "VK_F5",
    VK_F6 : "VK_F6",
    VK_F7 : "VK_F7",
    VK_F8 : "VK_F8",
    VK_F9 : "VK_F9",
    VK_F10 : "VK_F10",
    VK_F11 : "VK_F11",
    VK_F12 : "VK_F12",
    VK_F13 : "VK_F13",
    VK_F14 : "VK_F14",
    VK_F15 : "VK_F15",
    VK_F16 : "VK_F16",
    VK_F17 : "VK_F17",
    VK_F18 : "VK_F18",
    VK_F19 : "VK_F19",
    VK_F20 : "VK_F20",
    VK_F21 : "VK_F21",
    VK_F22 : "VK_F22",
    VK_F23 : "VK_F23",
    VK_F24 : "VK_F24",
    VK_NUMLOCK : "VK_NUMLOCK",
    VK_SCROLL : "VK_SCROLL",
    VK_LSHIFT : "VK_LSHIFT",
    VK_RSHIFT : "VK_RSHIFT",
    VK_LCONTROL : "VK_LCONTROL",
    VK_RCONTROL : "VK_RCONTROL",
    VK_LMENU : "VK_LMENU",
    VK_RMENU : "VK_RMENU",
    VK_OEM_NEC_EQUAL : "VK_OEM_NEC_EQUAL",
    VK_OEM_FJ_JISHO : "VK_OEM_FJ_JISHO",
    VK_OEM_FJ_MASSHOU : "VK_OEM_FJ_MASSHOU",
    VK_OEM_FJ_TOUROKU : "VK_OEM_FJ_TOUROKU",
    VK_OEM_FJ_LOYA : "VK_OEM_FJ_LOYA",
    VK_OEM_FJ_ROYA : "VK_OEM_FJ_ROYA",
    VK_BROWSER_BACK : "VK_BROWSER_BACK",
    VK_BROWSER_FORWARD : "VK_BROWSER_FORWARD",
    VK_BROWSER_REFRESH : "VK_BROWSER_REFRESH",
    VK_BROWSER_STOP : "VK_BROWSER_STOP",
    VK_BROWSER_SEARCH : "VK_BROWSER_SEARCH",
    VK_BROWSER_FAVORITES : "VK_BROWSER_FAVORITES",
    VK_BROWSER_HOME : "VK_BROWSER_HOME",
    VK_VOLUME_MUTE : "VK_VOLUME_MUTE",
    VK_VOLUME_DOWN : "VK_VOLUME_DOWN",
    VK_VOLUME_UP : "VK_VOLUME_UP",
    VK_MEDIA_NEXT_TRACK : "VK_MEDIA_NEXT_TRACK",
    VK_MEDIA_PREV_TRACK : "VK_MEDIA_PREV_TRACK",
    VK_MEDIA_STOP : "VK_MEDIA_STOP",
    VK_MEDIA_PLAY_PAUSE : "VK_MEDIA_PLAY_PAUSE",
    VK_LAUNCH_MAIL : "VK_LAUNCH_MAIL",
    VK_LAUNCH_MEDIA_SELECT : "VK_LAUNCH_MEDIA_SELECT",
    VK_LAUNCH_APP1 : "VK_LAUNCH_APP1",
    VK_LAUNCH_APP2 : "VK_LAUNCH_APP2",
    VK_OEM_1 : "VK_OEM_1",
    VK_OEM_PLUS : "VK_OEM_PLUS",
    VK_OEM_COMMA : "VK_OEM_COMMA",
    VK_OEM_MINUS : "VK_OEM_MINUS",
    VK_OEM_PERIOD : "VK_OEM_PERIOD",
    VK_OEM_2 : "VK_OEM_2",
    VK_OEM_3 : "VK_OEM_3",
    VK_OEM_4 : "VK_OEM_4",
    VK_OEM_5 : "VK_OEM_5",
    VK_OEM_6 : "VK_OEM_6",
    VK_OEM_7 : "VK_OEM_7",
    VK_OEM_8 : "VK_OEM_8",
    VK_OEM_AX : "VK_OEM_AX",
    VK_OEM_102 : "VK_OEM_102",
    VK_ICO_HELP : "VK_ICO_HELP",
    VK_ICO_00 : "VK_ICO_00",
    VK_PROCESSKEY : "VK_PROCESSKEY",
    VK_ICO_CLEAR : "VK_ICO_CLEAR",
    VK_PACKET : "VK_PACKET",
    VK_ATTN : "VK_ATTN",
    VK_CRSEL : "VK_CRSEL",
    VK_EXSEL : "VK_EXSEL",
    VK_EREOF : "VK_EREOF",
    VK_PLAY : "VK_PLAY",
    VK_ZOOM : "VK_ZOOM",
    VK_PA1 : "VK_PA1",
    VK_OEM_CLEAR : "VK_OEM_CLEAR",
    VK_OEM_RESET : "VK_OEM_RESET",
    VK_OEM_JUMP : "VK_OEM_JUMP",
    VK_OEM_PA1 : "VK_OEM_PA1",
    VK_OEM_PA2 : "VK_OEM_PA2",
    VK_OEM_PA3 : "VK_OEM_PA3",
    VK_OEM_WSCTRL : "VK_OEM_WSCTRL",
    VK_OEM_CUSEL : "VK_OEM_CUSEL",
    VK_OEM_ATTN : "VK_OEM_ATTN",
    VK_OEM_FINISH : "VK_OEM_FINISH",
    VK_OEM_COPY : "VK_OEM_COPY",
    VK_OEM_AUTO : "VK_OEM_AUTO",
    VK_OEM_ENLW : "VK_OEM_ENLW",
    VK_OEM_BACKTAB : "VK_OEM_BACKTAB",
    VK_ATTN : "VK_ATTN",
    VK_CRSEL : "VK_CRSEL",
    VK_EXSEL : "VK_EXSEL",
    VK_EREOF : "VK_EREOF",
    VK_PLAY : "VK_PLAY",
    VK_ZOOM : "VK_ZOOM",
    VK_NONAME : "VK_NONAME",
    VK_PA1 : "VK_PA1",
    VK_OEM_CLEAR : "VK_OEM_CLEAR"
}
