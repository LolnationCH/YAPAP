# YAPAP - Yet Another Python Automation Package

This is yet another automation package made in pure python for python use.

Why did I make this? Because I wanted to do some simple keystroke injection (Media keys), and before I knew it, I had full on mouse and keyboard input emulation and hook.
This project of media control is in `MediaControl.py`. It's specific to where I put my Chrome Youtube Music tab (the play button), the rest should work as intented.

## Features
**Windows only**
- Keyboard and Mouse hook
- Keyboard and Mouse input emulation
- Put focus on a Window with a pattern in the window title. (Note : Windows can't force focus (if your typing, or a program is requiring focus). If it can't focus, it will put a "notification" in the task bar (flashing the icon of the program))

Plans for the future :
- Raw Input -> Allows to see which device send input. Will allow to make a two keyboard setup useful (making a keyboard shortcuts only :) )
- Screenshot, allow to make decision based on image
- Stats for analyzing behavior (Hotspot for mouse, most pressed keys, etc.)
- Linux Support
- Mac Support (If really wanted)

## How to use
Example of use : `MediaControl.py`

Keyboard, Mouse and Window are imported in `YAPAP.py`, allowing you to simply do :
```
from YAPAP import Window, Keyboard, Mouse, importAllFrom
keyboard = Keyboard.Keyboard()
mouse = Mouse.Mouse()
.
.
.
```
`importAllFrom` allows you to import all from a module.

see the DevNote.md for more information