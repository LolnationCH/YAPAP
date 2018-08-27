'''
Example of program that can be made with this package
Allows user for global shortcut for media in case the keyboard he use does not comes with them
'''
# pylint: disable=line-too-long
# pylint: disable=undefined-variable
# pylint: disable=invalid-name
from YAPAP import Window, Keyboard, Mouse, import_from, import_from_lt

KEY_IS_PRESSED_WITH_ALT = lambda event: event.eventType == 'DOWN' and event.modifiers["ALT"]

def key_to_press_func(event):
    '''
    Function use in the callback of the listen function for the keyboard
    '''
    if KEY_IS_PRESSED_WITH_ALT(event):
        if event.vk in KEY_TO_PRESS:
            Keyboard.press_n_release_key(KEY_TO_PRESS[event.vk])
        elif event.vk == Keyboard.VK_KEY_S:
            if Window.findHandlesWindowWithPattern("YouTube Music", Window.SetForegroundWindow):
                Mouse.MoveTo(-752, 1023)
                Mouse.Click("Left")
    return True

KEY_TO_PRESS = {
    Keyboard.VK_KEY_U : Keyboard.VK_VOLUME_UP,
    Keyboard.VK_KEY_D : Keyboard.VK_VOLUME_DOWN,
    Keyboard.VK_KEY_M : Keyboard.VK_VOLUME_MUTE
}


if __name__ == "__main__":
    Keyboard.listen(key_to_press_func)
