'''
Window const
'''

# pylint: disable=bad-whitespace
# pylint: disable=line-too-long
# Flags and Code for SetWindowPos

HWND_INSERT_AFTER = {
    "HWND_BOTTOM"    : 1,  # Places the window at the bottom of the Z order. If the hWnd parameter identifies a topmost window, the window loses its topmost status and is placed at the bottom of all other windows.
    "HWND_NOTOPMOST" : -2, # Places the window above all non-topmost windows (that is, behind all topmost windows). This flag has no effect if the window is already a non-topmost window.
    "HWND_TOP"       : 0,  # Places the window at the top of the Z order.
    "HWND_TOPMOST"   : -1, # Places the window above all non-topmost windows. The window maintains its topmost position even when it is deactivated.
}
# The following codes can be added together
UFLAGS_SET_WINDOWS_POS = {
    "SWP_ASYNCWINDOWPOS" : 0x4000, # If the calling thread and the thread that owns the window are attached to different input queues, the system posts the request to the thread that owns the window. This prevents the calling thread from blocking its execution while other threads process the request.
    "SWP_DEFERERASE"     : 0x2000, # Prevents generation of the WM_SYNCPAINT message.
    "SWP_DRAWFRAME"      : 0x0020, # Draws a frame (defined in the window's class description) around the window.
    "SWP_FRAMECHANGED"   : 0x0020, # Applies new frame styles set using the SetWindowLong function. Sends a WM_NCCALCSIZE message to the window, even if the window's size is not being changed. If this flag is not specified, WM_NCCALCSIZE is sent only when the window's size is being changed.
    "SWP_HIDEWINDOW"     : 0x0080, # Hides the window.
    "SWP_NOACTIVATE"     : 0x0010, # Does not activate the window. If this flag is not set, the window is activated and moved to the top of either the topmost or non-topmost group (depending on the setting of the hWndInsertAfter parameter).
    "SWP_NOCOPYBITS"     : 0x0100, # Discards the entire contents of the client area. If this flag is not specified, the valid contents of the client area are saved and copied back into the client area after the window is sized or repositioned.
    "SWP_NOMOVE"         : 0x0002, # Retains the current position (ignores X and Y parameters).
    "SWP_NOOWNERZORDER"  : 0x0200, # Does not change the owner window's position in the Z order.
    "SWP_NOREDRAW"       : 0x0008, # Does not redraw changes. If this flag is set, no repainting of any kind occurs. This applies to the client area, the nonclient area (including the title bar and scroll bars), and any part of the parent window uncovered as a result of the window being moved. When this flag is set, the application must explicitly invalidate or redraw any parts of the window and parent window that need redrawing.
    "SWP_NOREPOSITION"   : 0x0200, # Same as the SWP_NOOWNERZORDER flag.
    "SWP_NOSENDCHANGING" : 0x0400, # Prevents the window from receiving the WM_WINDOWPOSCHANGING message.
    "SWP_NOSIZE"         : 0x0001, # Retains the current size (ignores the cx and cy parameters).
    "SWP_NOZORDER"       : 0x0004, # Retains the current Z order (ignores the hWndInsertAfter parameter).
    "SWP_SHOWWINDOW"     : 0x0040, # Displays
}


# Flags and Code for WINDOWPLACEMENT
WINDOW_PLACEMENT_FLAGS = {
    "WPF_ASYNCWINDOWPLACEMENT" : 0x0004, # If the calling thread and the thread that owns the window are attached to different input queues, the system posts the request to the thread that owns the window. This prevents the calling thread from blocking its execution while other threads process the request.
    "WPF_RESTORETOMAXIMIZED"   : 0x0002, # The restored window will be maximized, regardless of whether it was maximized before it was minimized. This setting is only valid the next time the window is restored. It does not change the default restoration behavior. This flag is only valid when the SW_SHOWMINIMIZED value is specified for the showCmd member.
    "WPF_SETMINPOSITION"       : 0x0001 # The coordinates of the minimized window may be specified. This flag must be specified if the coordinates are set in the ptMinPosition member.
}

WINDOW_PLACEMENT_SHOWCMD = {
    "SW_HIDE"            : 0, # Hides the window and activates another window.
    "SW_MAXIMIZE"        : 3, # Maximizes the specified window.
    "SW_MINIMIZE"        : 6, # Minimizes the specified window and activates the next top-level window in the z-order.
    "SW_RESTORE"         : 9, # Activates and displays the window. If the window is minimized or maximized, the system restores it to its original size and position. An application should specify this flag when restoring a minimized window.
    "SW_SHOW"            : 5, # Activates the window and displays it in its current size and position.
    "SW_SHOWMAXIMIZED"   : 3, # Activates the window and displays it as a maximized window.
    "SW_SHOWMINIMIZED"   : 2, # Activates the window and displays it as a minimized window.
    "SW_SHOWMINNOACTIVE" : 7, # Displays the window as a minimized window. This value is similar to SW_SHOWMINIMIZED, except the window is not activated.
    "SW_SHOWNA"          : 8, # Displays the window in its current size and position. This value is similar to SW_SHOW, except the window is not activated.
    "SW_SHOWNOACTIVATE"  : 4, # Displays a window in its most recent size and position. This value is similar to SW_SHOWNORMAL, except the window is not activated.
    "SW_SHOWNORMAL"      : 1 # Activates and displays a window. If the window is minimized or maximized, the system restores it to its original size and position. An application should specify this flag when displaying the window for the first time.
}
