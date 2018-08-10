# Filename : MouseScanCode.py 
# Desc. : Scan codes for mouse
#
# ----------------------------------------------------------------------------------# 

# dwFlags for MOUSEINPUT
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646273(v=vs.85).aspx
MOUSEEVENTF_MOVE        = 0x0001
MOUSEEVENTF_LEFTDOWN    = 0x0002
MOUSEEVENTF_LEFTUP      = 0x0004
MOUSEEVENTF_RIGHTDOWN   = 0x0008
MOUSEEVENTF_RIGHTUP     = 0x0010
MOUSEEVENTF_MIDDLEDOWN  = 0x0020
MOUSEEVENTF_MIDDLEUP    = 0x0040

MOUSEEVENTF_VIRTUALDESK = 0x4000 # Maps coordinates to the entire desktop. Must be used with MOUSEEVENTF_ABSOLUTE.
MOUSEEVENTF_WHEEL       = 0x0800 # The wheel was moved, if the mouse has a wheel. The amount of movement is specified in mouseData.
MOUSEEVENTF_XDOWN       = 0x0080 # An X button was pressed. XBUTTON1 or XBUTTON2 needs to be specify
MOUSEEVENTF_XUP         = 0x0100 # An X button was released. XBUTTON1 or XBUTTON2 needs to be specify
MOUSEEVENTF_ABSOLUTE    = 0x8000
MOUSEEVENTF_HWHEEL      = 0x1000

# From https://github.com/boppreh/keyboard/blob/master/keyboard/_winmouse.py
# Beware, as of 2016-01-30 the official docs have a very incomplete list.
# This one was compiled from experience and may be incomplete.
# Me : Check if this is still the case : https://docs.microsoft.com/en-us/windows/desktop/inputdev/mouse-input-notifications
WM_MOUSEMOVE = 0x200

WM_LBUTTONDOWN = 0x201
WM_LBUTTONUP = 0x202
WM_LBUTTONDBLCLK = 0x203

WM_RBUTTONDOWN = 0x204
WM_RBUTTONUP = 0x205
WM_RBUTTONDBLCLK = 0x206

WM_MBUTTONDOWN = 0x207
WM_MBUTTONUP = 0x208
WM_MBUTTONDBLCLK = 0x209

WM_MOUSEWHEEL = 0x20A
WM_XBUTTONDOWN = 0x20B
WM_XBUTTONUP = 0x20C
WM_XBUTTONDBLCLK = 0x20D
WM_MOUSEHWHEEL = 0x20E

WM_NCXBUTTONDOWN = 0x00AB
WM_NCXBUTTONUP = 0x00AC
WM_NCXBUTTONDBLCLK = 0x00AD

# Parameters for Simulation and Hooking
WHEEL_DELTA = 120

LEFT = 'Left'
RIGHT = 'Right'
MIDDLE = 'Middle'
X = 'X'
X2 = 'X2'
VERTICAL = 'Vertical'
HORIZONTAL = 'Horizontal'

UP = 'UP'
DOWN = 'DOWN'
DOUBLE = 'DOUBLE'
WHEEL = 'WHEEL'

# Dictionary for the dwFlags MOUSEINPUT
inputMouseButton = { 
   DOWN : {
        LEFT   : MOUSEEVENTF_LEFTDOWN,
        RIGHT  : MOUSEEVENTF_RIGHTDOWN,
        MIDDLE : MOUSEEVENTF_MIDDLEDOWN,
        X      : MOUSEEVENTF_XDOWN,
        X2     : MOUSEEVENTF_XDOWN
    },
   UP : {
        LEFT   : MOUSEEVENTF_LEFTUP,
        RIGHT  : MOUSEEVENTF_RIGHTUP,
        MIDDLE : MOUSEEVENTF_MIDDLEUP,
        X      : MOUSEEVENTF_XUP,
        X2     : MOUSEEVENTF_XUP
    },
   WHEEL : {
        VERTICAL   : MOUSEEVENTF_WHEEL,
        HORIZONTAL : MOUSEEVENTF_HWHEEL,
    }
}

wmCodeButton = {
    WM_LBUTTONDOWN   : (DOWN, LEFT),
    WM_LBUTTONUP     : (UP, LEFT),
    WM_LBUTTONDBLCLK : (DOUBLE, LEFT),

    WM_RBUTTONDOWN   : (DOWN, RIGHT),
    WM_RBUTTONUP     : (UP, RIGHT),
    WM_RBUTTONDBLCLK : (DOUBLE, RIGHT),

    WM_MBUTTONDOWN   : (DOWN, MIDDLE),
    WM_MBUTTONUP     : (UP, MIDDLE),
    WM_MBUTTONDBLCLK : (DOUBLE, MIDDLE),

    WM_XBUTTONDOWN   : (DOWN, X),
    WM_XBUTTONUP     : (UP, X),
    WM_XBUTTONDBLCLK : (DOUBLE, X),
}