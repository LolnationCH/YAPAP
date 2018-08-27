'''
Scan codes for xInput
'''

# pylint: disable=bad-whitespace

# Bitmasks for the joysticks buttons, determines what has
# been pressed on the joystick, these need to be mapped
# to whatever device you're using instead of an xbox 360
# joystick

XINPUT_GAMEPAD_DPAD_UP        = 0x0001
XINPUT_GAMEPAD_DPAD_DOWN      = 0x0002
XINPUT_GAMEPAD_DPAD_LEFT      = 0x0004
XINPUT_GAMEPAD_DPAD_RIGHT     = 0x0008
XINPUT_GAMEPAD_START          = 0x0010
XINPUT_GAMEPAD_BACK           = 0x0020
XINPUT_GAMEPAD_LEFT_THUMB     = 0x0040
XINPUT_GAMEPAD_RIGHT_THUMB    = 0x0080
XINPUT_GAMEPAD_LEFT_SHOULDER  = 0x0100
XINPUT_GAMEPAD_RIGHT_SHOULDER = 0x0200
XINPUT_GAMEPAD_A              = 0x1000
XINPUT_GAMEPAD_B              = 0x2000
XINPUT_GAMEPAD_X              = 0x4000
XINPUT_GAMEPAD_Y              = 0x8000

# Defines the flags used to determine if the user is pushing
# down on a button, not holding a button, etc

XINPUT_KEYSTROKE_KEYDOWN = 0x0001
XINPUT_KEYSTROKE_KEYUP   = 0x0002
XINPUT_KEYSTROKE_REPEAT  = 0x0004

# Defines the codes which are returned by XInputGetKeystroke


VK_PAD_A                = 0x5800
VK_PAD_B                = 0x5801
VK_PAD_X                = 0x5802
VK_PAD_Y                = 0x5803
VK_PAD_RSHOULDER        = 0x5804
VK_PAD_LSHOULDER        = 0x5805
VK_PAD_LTRIGGER         = 0x5806
VK_PAD_RTRIGGER         = 0x5807
VK_PAD_DPAD_UP          = 0x5810
VK_PAD_DPAD_DOWN        = 0x5811
VK_PAD_DPAD_LEFT        = 0x5812
VK_PAD_DPAD_RIGHT       = 0x5813
VK_PAD_START            = 0x5814
VK_PAD_BACK             = 0x5815
VK_PAD_LTHUMB_PRESS     = 0x5816
VK_PAD_RTHUMB_PRESS     = 0x5817
VK_PAD_LTHUMB_UP        = 0x5820
VK_PAD_LTHUMB_DOWN      = 0x5821
VK_PAD_LTHUMB_RIGHT     = 0x5822
VK_PAD_LTHUMB_LEFT      = 0x5823
VK_PAD_LTHUMB_UPLEFT    = 0x5824
VK_PAD_LTHUMB_UPRIGHT   = 0x5825
VK_PAD_LTHUMB_DOWNRIGHT = 0x5826
VK_PAD_LTHUMB_DOWNLEFT  = 0x5827
VK_PAD_RTHUMB_UP        = 0x5830
VK_PAD_RTHUMB_DOWN      = 0x5831
VK_PAD_RTHUMB_RIGHT     = 0x5832
VK_PAD_RTHUMB_LEFT      = 0x5833
VK_PAD_RTHUMB_UPLEFT    = 0x5834
VK_PAD_RTHUMB_UPRIGHT   = 0x5835
VK_PAD_RTHUMB_DOWNRIGHT = 0x5836
VK_PAD_RTHUMB_DOWNLEFT  = 0x5837

# Deadzones are for analogue joystick controls on the joypad
# which determine when input should be assumed to be in the
# middle of the pad. This is a threshold to stop a joypad
# controlling the game when the player isn't touching the
# controls.

XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE   = 7849
XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE  = 8689
XINPUT_GAMEPAD_TRIGGER_THRESHOLD     = 30

# Defines what type of abilities the type of joystick has
# DEVTYPE_GAMEPAD is available for all joysticks, however
# there may be more specific identifiers for other joysticks
# which are being used.

XINPUT_DEVTYPE_GAMEPAD         = 0x01
XINPUT_DEVSUBTYPE_GAMEPAD      = 0x01
XINPUT_DEVSUBTYPE_WHEEL        = 0x02
XINPUT_DEVSUBTYPE_ARCADE_STICK = 0x03
XINPUT_DEVSUBTYPE_FLIGHT_SICK  = 0x04
XINPUT_DEVSUBTYPE_DANCE_PAD    = 0x05
XINPUT_DEVSUBTYPE_GUITAR       = 0x06
XINPUT_DEVSUBTYPE_DRUM_KIT     = 0x08


# These are used with the XInputGetCapabilities function to
# determine the abilities to the joystick which has been
# plugged in.

XINPUT_CAPS_VOICE_SUPPORTED = 0x0004
XINPUT_FLAG_GAMEPAD         = 0x00000001

# Defines the status of the battery if one is used in the
# attached joystick. The first two define if the joystick
# supports a battery. Disconnected means that the joystick
# isn't connected. Wired shows that the joystick is a wired
# joystick.

BATTERY_DEVTYPE_GAMEPAD   = 0x00
BATTERY_DEVTYPE_HEADSET   = 0x01
BATTERY_TYPE_DISCONNECTED = 0x00
BATTERY_TYPE_WIRED        = 0x01
BATTERY_TYPE_ALKALINE     = 0x02
BATTERY_TYPE_NIMH         = 0x03
BATTERY_TYPE_UNKNOWN      = 0xFF
BATTERY_LEVEL_EMPTY       = 0x00
BATTERY_LEVEL_LOW         = 0x01
BATTERY_LEVEL_MEDIUM      = 0x02
BATTERY_LEVEL_FULL        = 0x03

# How many joysticks can be used with this library. Games that
# use the xinput library will not go over this number.

XUSER_MAX_COUNT = 4
XUSER_INDEX_ANY = 0x000000FF
