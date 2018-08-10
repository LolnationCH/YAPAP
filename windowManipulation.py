import ctypes

from functions import WNDENUMPROC, GetWindowTextLengthW, GetWindowTextW, EnumWindows, SetForegroundWindow

def list_windows(patternToFind):
    lt_ret = []
    def worker(hwnd, lParam):
        stre = GetWindowTextW(hwnd)
        if stre != '' and stre != "Default IME" and stre != "MSCTFIME UI":
            if stre.find(patternToFind) != -1:
                lt_ret.append(True)
                SetForegroundWindow(hwnd)
        return True

    cb_worker = WNDENUMPROC(worker)
    if not EnumWindows(cb_worker, 42):
        raise ctypes.WinError()
    return len(lt_ret)