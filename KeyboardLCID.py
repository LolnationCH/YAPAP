# Filename : KeyboardLCID.py
# Desc. : Determine the keyboard layout and info
#
#-------------------------------   REFERENCE ---------------------------------------#
#
# Appendix A: Product Behavior
# https://msdn.microsoft.com/en-us/library/cc233982.aspx
# ----------------------------------------------------------------------------------#
#
# Language Identifiers
# https://docs.microsoft.com/fr-fr/windows/desktop/Intl/language-identifiers
#
#            +-------------------------+-------------------------+
#            |     SubLanguage ID      |   Primary Language ID   |
#            +-------------------------+-------------------------+
#            15                    10  9                         0   bit
#
# ----------------------------------------------------------------------------------#
from functions import user32

class KeyboardLCID():
    def __init__(self):
        import csv
        self.KeyboardLCID = {}
        with open("keyboardLCID.csv", newline='\n') as f:
            data = csv.DictReader(f)
            for x in data:
                self.KeyboardLCID[x["Language ID"]] = x

        # Get Keyboard layout
        curr_window = user32.GetForegroundWindow()
        thread_id = user32.GetWindowThreadProcessId(curr_window, 0)

        self.KeyboardLayout = user32.GetKeyboardLayout(thread_id)
        self.KeyboardLayout = user32.GetKeyboardLayout(0) if self.KeyboardLayout == 0 else self.KeyboardLayout

    def GetKeyboard(self, LCID):
        return self.KeyboardLCID[LCID]

    # Extract language ID from KLID
    # Then convert language ID from decimal to hexadecimal
    # Search which keyboard is used
    def GetKeyboardInfo(self):
        return self.GetKeyboard(hex(self.KeyboardLayout & (2**16 - 1)))
