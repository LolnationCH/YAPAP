'''
Keyboard Event definition and parsing
'''
#pylint: disable=too-many-arguments
#pylint: disable=invalid-name
from time import time as GetTime

def parseEvent(stre, last_time):
    '''Parse a keyboard event from a str.'''
    rest = stre[17:].split(',')
    eventType = rest[0][10:]
    vk = int(rest[1][4:])
    time = float(rest[2][5:]) - last_time
    return KeyboardEvent(eventType, vk, time=time), float(rest[2][5:])



class KeyboardEvent():
    '''Keyboard Event container.'''
    def __init__(self, eventType, vk, name=None, modifiers=None, isKeypad=None, time=None):
        '''init with current time if None were specify.'''
        self.eventType = eventType
        self.vk = vk
        self.name = name
        self.modifiers = modifiers
        self.isKeypad = isKeypad
        self.time = time if time is not None else GetTime()

    def __str__(self):
        '''Used for writing in the file.'''
        return 'KeyboardEvent => EventType:{},vk: {},time={}'.format(self.eventType,
                                                                     self.vk, self.time)

    def __eq__(self, other):
        '''To compare keys between each other.'''
        return isinstance(other, KeyboardEvent) and self.eventType == other.eventType \
                                                and self.vk == other.vk
