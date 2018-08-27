'''
Module for windows manipulation.
'''
import ctypes

from .Functions import WNDENUMPROC, GetWindowTextW, EnumWindows, GetWindowRect, SetWindowPos
# These are to make them available through this module, not to be used by it
# pylint: disable=unused-import
from .Functions import MinimizeWindow, DestroyWindow, FindWindow, SetForegroundWindow
# pylint: enable=unused-import
from .codes.WindowConst import UFLAGS_SET_WINDOWS_POS

def _calc_uflags_window_pos(insert_after=None, tuple_pos=None, tuple_size=None, lt_flags=None):
    '''
    Calculate the value of the flag based on the list and the parameter available
    '''
    ret = (0 if insert_after is not None else UFLAGS_SET_WINDOWS_POS['SWP_NOZORDER']) \
        | (0 if tuple_pos is not None else UFLAGS_SET_WINDOWS_POS['SWP_NOMOVE']) \
        | (0 if tuple_size is not None else UFLAGS_SET_WINDOWS_POS['SWP_NOSIZE'])

    for flag in lt_flags:
        if flag in UFLAGS_SET_WINDOWS_POS:
            ret |= UFLAGS_SET_WINDOWS_POS[flag]
    return ret

def _none_to_zero_tuple(val):
    '''
    Make a None value to a tuple of Zero
    '''
    return (0, 0) if val is None else val

# Naming convention to follow the one use by Windows
# Look is this could be change if linux and max dont followe these
# pylint: disable=invalid-name
def getWindowSize(hwnd):
    '''
    Return the current size of the handled window
    '''
    dim = GetWindowRect(hwnd)
    width = dim.right - dim.left + 1
    height = dim.bottom - dim.top + 1
    return width, height

def getWindowPos(hwnd):
    '''
    Return the current position of the handled window
    '''
    dim = GetWindowRect(hwnd)
    return dim.left, dim.top

def setWindow(hwnd, insert_after=None, tuple_pos=None, tuple_size=None, lt_flags=None):
    '''
    Set the position and size of the window, among other things
    '''
    flag = _calc_uflags_window_pos(insert_after, tuple_pos, tuple_size, lt_flags)
    SetWindowPos(hwnd, 0 if insert_after is None else insert_after,
                 _none_to_zero_tuple(tuple_pos)[0], _none_to_zero_tuple(tuple_pos)[1],
                 _none_to_zero_tuple(tuple_size)[0], _none_to_zero_tuple(tuple_size)[1], flag)

# The default empty list is not dangerous,
# no assignement done, only iteration (can't be done with None)
# pylint: disable=dangerous-default-value
def setWindowPos(hwnd, tuple_pos, insert_after=None, lt_flags=[]):
    '''
    Set the position of the window
    '''
    return setWindow(hwnd, insert_after=insert_after,
                     tuple_pos=tuple_pos, lt_flags=lt_flags)

def setWindowSize(hwnd, tuple_size, insert_after=None, lt_flags=[]):
    '''
    Set the size of the window
    '''
    return setWindow(hwnd, insert_after=insert_after,
                     tuple_size=tuple_size, lt_flags=lt_flags)
# pylint: enable=dangerous-default-value


def findHandlesWindowWithPattern(patternToFind, func=None):
    '''
    Find the handle(s) matching the pattern, can also applied a function to all the handle
    the function needs to take only the handle
    '''
    lt_handles = []
    def worker(hwnd, _):
        stre = GetWindowTextW(hwnd)
        if stre not in ['', "Default IME", "MSCTFIME UI"] and stre.find(patternToFind) != -1:
            if func is not None:
                func(hwnd)
            lt_handles.append(hwnd)
        return True

    cb_worker = WNDENUMPROC(worker)
    if not EnumWindows(cb_worker, 42):
        raise ctypes.WinError()
    return lt_handles
