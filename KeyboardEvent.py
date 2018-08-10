from time import time as GetTime

def parseEvent(stre, last_time):    
    try:
        rest = stre[17:].split(',')
        eventType = rest[0][10:]
        vk = int(rest[1][4:])
        time = float(rest[2][5:]) - last_time
        return KeyboardEvent(eventType, vk, time=time), float(rest[2][5:])
    except Exception as e:
        print(e)
        return None, last_time



class KeyboardEvent(object):
    def __init__(self, eventType, vk, name=None, modifiers=None, isKeypad=None, time=None):
        self.eventType = eventType
        self.vk = vk
        self.name = name
        self.modifiers = modifiers
        self.isKeypad = isKeypad
        self.time = time if time != None else GetTime()

    def __str__(self):
        return 'KeyboardEvent => EventType:{},vk: {},time={}'.format(self.eventType, self.vk, self.time)

    def __eq__(self, other):
        return isinstance(other, KeyboardEvent) and self.eventType == other.eventType and self.vk == other.vk