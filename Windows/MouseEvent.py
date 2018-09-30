'''
Containers for the different event available to the mouse
'''
#pylint: disable=too-few-public-methods
#pylint: disable=invalid-name

from .codes.MouseScanCode import WM_CODE_BUTTON

#pylint: disable=invalid-name
def parse_event(stre, last_time):
    '''Parse events written in a file. Must follow the standard in __str__ below'''
    class_t = stre[:10]
    rest = stre[14:].split(',')
    if class_t == "MovesEvent":
        x = int(rest[0][3:])
        y = int(rest[1][3:])
        time = float(rest[2][5:]) - last_time
        return MoveEvent(x, y, time), float(rest[2][5:])
    if class_t == "WheelEvent":
        delta = float(rest[0][7:])
        time = float(rest[1][5:]) - last_time
        return WheelEvent(delta, time), float(rest[1][5:])
    if class_t == "ClickEvent":
        code = int(rest[0][6:])
        data = int(rest[1][6:])
        time = float(rest[2][5:]) - last_time
        return ButtonEvent(code, data, time), float(rest[2][5:])
    print(stre)
    return None, last_time


# The name for the __str__ do not match the class name simply for length convention
# I could make it more complicated, but for now that will do

class MoveEvent():
    '''Move event info container.'''
    def __init__(self, x, y, time):
        '''..'''
        self.X = x
        self.Y = y
        self.time = time

    def __str__(self):
        '''Standard Representation for this event, to be written in a file.'''
        return "MovesEvent => X: {},Y: {},time={}".format(self.X, self.Y, self.time)
#pylint: enable=invalid-name

class WheelEvent():
    '''Wheel event info container.'''
    def __init__(self, delta, time):
        '''.'''
        self.delta = delta
        self.time = time

    def __str__(self):
        '''Standard Representation for this event, to be written in a file..'''
        return "WheelEvent => delta: {},time={}".format(self.delta, self.time)

class ButtonEvent():
    '''Button event info container.'''
    def __init__(self, code, data, time):
        '''.'''
        self.event_type, self.button = WM_CODE_BUTTON[code]
        self.code = code
        self.data = data
        self.time = time

    def __str__(self):
        '''Standard Representation for this event, to be written in a file..'''
        return "ClickEvent => code: {},data: {},time={}".format(self.code, self.data, self.time)
