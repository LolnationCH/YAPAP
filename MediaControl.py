import os
import ctypes

from Keyboard import *
from Mouse import *
import windowManipulation
from functions import BlockInput

clear = lambda: os.system('cls')

def keyIsPressedWithAlt(event):
    return event.eventType == KEY_DOWN and event.modifiers["ALT"]

m = Mouse()

def keyToPressFunc(event):
    if keyIsPressedWithAlt(event):
        if event.vk in keyToPress:
            lst_time = event.time
            k.PressNReleaseKey(keyToPress[event.vk])
        elif event.vk == VK_KEY_S:
            if windowManipulation.list_windows("YouTube Music"):
                m.MoveTo(-752, 1023)
                m.Click("Left")
    return True

keyToPress = {
                VK_KEY_U : VK_VOLUME_UP,
                VK_KEY_D : VK_VOLUME_DOWN,
                VK_KEY_M : VK_VOLUME_MUTE
             }


if __name__ == "__main__":
    k = Keyboard()
    k.listen(keyToPressFunc)