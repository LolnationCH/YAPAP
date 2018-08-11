# Filename : mouseEvent.py
# Desc. : Containers for the different event available to the mouse
#
# ----------------------------------------------------------------------------------#

from codes.MouseScanCode import *

def parseEvent(stre, last_time):
    try:
        classT = stre[:10]
        rest = stre[14:].split(',')
        if classT == "MovesEvent":
            x = int(rest[0][3:])
            y = int(rest[1][3:])
            time = float(rest[2][5:]) - last_time
            return MoveEvent(x,y,time), float(rest[2][5:])
        elif classT == "WheelEvent":
            delta = float(rest[0][7:])
            time = float(rest[1][5:]) - last_time
            return WheelEvent(delta,time), float(rest[1][5:])
        elif classT == "ClickEvent":
            code = int(rest[0][6:])
            data = int(rest[1][6:])
            time = float(rest[2][5:]) - last_time
            return ButtonEvent(code,data,time), float(rest[2][5:])
        else:
            print(stre)
    except Exception as e:
        print(e)
        return None, last_time


# The name for the __str__ do not match the class name simply for length convention
# I could make it more complicated, but for now that will do

class MoveEvent():
    def __init__(self, x, y, time):
        self.X = x
        self.Y = y
        self.time = time

    def __str__(self):
        return "MovesEvent => X: {},Y: {},time={}".format(self.X, self.Y, self.time)

class WheelEvent():
    def __init__(self, delta, time):
        self.delta = delta
        self.time = time

    def __str__(self):
        return "WheelEvent => delta: {},time={}".format(self.delta, self.time)

class ButtonEvent():
    def __init__(self, code, data, time):
        self.event_type, self.button = wmCodeButton[code]
        self.code = code
        self.data = data
        self.time = time

    def __str__(self):
        return "ClickEvent => code: {},data: {},time={}".format(self.code, self.data, self.time)