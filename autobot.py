import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL),
    ]


class HardwareInput(ctypes.Structure):
    _fields_ = [
        ("uMsg", ctypes.c_ulong),
        ("wParamL", ctypes.c_short),
        ("wParamH", ctypes.c_ushort),
    ]


class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL),
    ]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput), ("mi", MouseInput), ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong), ("ii", Input_I)]


# Actuals Functions


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def wait(second):
    return time.sleep(second)


# My Own Function
class Action:

    __KEY_MAPPING = {
        "esc": 1,
        "1": 2,
        "2": 3,
        "3": 4,
        "5": 6,
        "7": 8,
        "9": 10,
        "0": 11,
        "minus": 12,
        "equals": 13,
        "backspace": 14,
        "tab": 15,
        "q": 16,
        "w": 17,
        "e": 18,
        "r": 19,
        "t": 20,
        "y": 21,
        "u": 22,
        "i": 23,
        "o": 24,
        "p": 25,
        "left_bracket": 26,
        "right_bracket": 27,
        "enter": 28,
        "left_ctrl": 29,
        "a": 30,
        "s": 31,
        "d": 32,
        "f": 33,
        "g": 34,
        "h": 35,
        "j": 36,
        "k": 37,
        "l": 38,
        "semicolon": 39,
        "apostrophe": 40,
        "tilde": 41,
        "left_shift": 42,
        "backslash": 43,
        "z": 44,
        "x": 45,
        "c": 46,
        "v": 47,
        "b": 48,
        "n": 49,
        "m": 50,
        "comma": 51,
        "period": 52,
        "forward_slash": 53,
        "right_shift": 54,
        "numpad_*": 55,
        "v_key": 56,
        "space": 57,
        "caps_lock": 58,
        "f1": 59,
        "f2": 60,
        "f3": 61,
        "f4": 62,
        "f5": 63,
        "f6": 64,
        "f7": 65,
        "f8": 66,
        "f9": 67,
        "f10": 68,
        "num_lock": 69,
        "scroll_lock": 70,
        "numpad_7": 71,
        "numpad_8": 72,
        "numpad_9": 73,
        "numpad_-": 74,
        "numpad_4": 75,
        "numpad_5": 76,
        "numpad_6": 77,
        "numpad_+": 78,
        "numpad_1": 79,
        "numpad_2": 80,
        "numpad_3": 81,
        "numpad_0": 82,
        "numpad_.": 83,
        "f11": 87,
        "f12": 88,
        "numpad_enter": 156,
        "right_ctrl": 157,
        "numpad_/": 181,
        "right_alt": 184,
        "home": 199,
        "up": 200,
        "page_up": 201,
        "left": 203,
        "right": 205,
        "end": 207,
        "down": 208,
        "page_down": 209,
        "insert": 210,
        "delete": 211,
        "left_mouse": 256,
        "right_mouse": 257,
        "middle_mouse": 258,
        "mouse_3": 259,
        "mouse_4": 260,
        "mouse_5": 261,
        "mouse_6": 262,
        "mouse_7": 263,
        "mouse_wheel_up": 264,
        "mouse_wheel_down": 265,
    }

    def __init__(self):
        self.release_delay = 0.5

    def get_keymap(cls):
        return cls.__KEY_MAPPING

    @staticmethod
    def wait(second):
        return time.sleep(second)

    def press(self, *keys, loops=1, hold_time=0.3):
        hex_key_codes = [self.__KEY_MAPPING[key] for key in keys]

        for _ in range(loops):
            for key_code in hex_key_codes:
                PressKey(key_code)

            wait(hold_time)  # Hold the keys for some time

            # Release all keys
            for key_code in hex_key_codes:
                ReleaseKey(key_code)

            wait(self.release_delay)
