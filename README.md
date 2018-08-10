# YAPAP - Yet Another Python Automation Package

This is yet another automation package made in pure python for python use.

Why did I make this? Because I wanted to do some simple keystroke injection (Media keys), and before I knew it, I had full on mouse and keyboard input emulation and hook.
This project of media control is in MediaControl.py. It's specific to where I put my Chrome Youtube Music tab (the play button), the rest should work as intented.

## Features
**Windows only**
- Keyboard and Mouse hook
- Keyboard and Mouse input emulation
- Put focus on a Window with a patter in the window title. (Note : Windows can't force focus (if your typing, or a program is requiring focus). If it can't focus, it will put a "notification" in the task bar (flashing the icon of the program))

Plans for the future :
- Raw Input -> Allows to see which device send input. Will allow to make a two keyboard setup useful (making a keyboard shortcuts only :) )
- Screenshot, allow to make decision based on image
- Stats for analyzing behavior (Hotspot for mouse, most pressed keys, etc.)
- Linux Support
- Mac Support (If really wanted)

## How to use
Example of use : MediaControl.py

Main modules : Mouse and Keyboard

Needs some refactoring for naming standards. If you see this text, either is not done yet (and should not use this package), either I forgot to remove this warning (lol). But look at what is available for both Mouse and Keyboard. The functions names are pretty explicit.

### Keyboard
**hex codes are required** (can be found in codes/KbdScanCode)

Keyboard have PressKey and ReleaseKey (Useful for modifiers like shift). For keys like letter, number, media_keys, etc... use PressNReleaseKey instead (It just do the two previous mention function).

**Pass unicode value as a int**

For unicode, use SendUnicodeChar. If you want a text to be type, use InputText. For hooking the keyboard, use listen. You need to pass a function (example are availaible at the top of the file), it needs to return a bool (if you are to continue or not)

writeToFileEvents can be pass to listen, this will produce a file that can be use with DoInputsRespectDelay or FastInputs.

### Mouse
Mouse is easier to look at. This section is to be done.

HookMouse to hook, function passed does not need to return a bool.

## Notes
If you are interested in how I made this, look in the function.py, struct.py and the codes folder. I put many URL link for the doc reference, in case they are needed.
