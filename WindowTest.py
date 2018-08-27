'''
Example for windows manipulation
'''
from YAPAP import Window, import_from_lt
globals().update(import_from_lt("functions", ["SetWindowPos"]))


if __name__ == "__main__":
    HANDLES = Window.findHandlesWindowWithPattern("Notepad++")
    #SetWindowPos(lt[0], 0, 0, 0, 150, 150,
    #             calculate_uFlagsSetWindowPos(['SWP_NOSIZE','SWP_SHOWWINDOW', 'SWP_NOMOVE']))
    print(Window.FindWindow(None, r"D:\YAPAP\YAPAP-master\WindowTest.py - Notepad++") in HANDLES)
