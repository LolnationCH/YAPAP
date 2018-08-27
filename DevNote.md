# Notes of developement


## Devices class

For each platform, the devices class needs to have these public class : 

**Keyboard specific - Input Emulation**
- PressNReleaseKey (hex code for key)
- PressKey         (hex code for key)
- ReleaseKey       (hex code for key)
- SendUnicodeChar  (unicode for char)
- InputText        (string of text  )

**Mouse specific - Input Emulation**
- MoveRelative     (x,y coord        )
- MoveWheel        (delta of movement)
- MoveTo           (x,y coord        )
- Click            (string, side     )

**Mouse specific - Hooking**
- GetPosition       *give mouse position*

**Hooking**
- Listen           (function callback)

**From file to emulation**
- DoInputsRespectDelay (filePath)
- FastInputs           (filePath)

## Codes

Virtual key, codes, identifiers, const values, etc... should be place in the `codes` folder for it's specific platform

The current implementation as of 14/08/2018 of the Windows KeyboardEvent `__str__` needs refactoring to respect that.
Idea to respect it would be a common list of id values, that will be assign to each vk of each platform, to be used when showing instead of the hex code.

## Examples and test
`MediaControl.py` is an example utilizing most of the common function.
Will need to make another example utilizing the rest of the common function.

Unit testing also needs to be implemented. The testing will be tough to be done alone, it will require the help of the internet.