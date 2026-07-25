"""Windows SendInput backend."""

import ctypes


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


class InputUnion(ctypes.Union):
    _fields_ = [
        ("ki", KeyBdInput),
        ("mi", MouseInput),
        ("hi", HardwareInput),
    ]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong), ("ii", InputUnion)]


def _send_input():
    try:
        return ctypes.windll.user32.SendInput
    except AttributeError as error:
        raise OSError("Game automation input requires Windows") from error


class WindowsInput:
    """Emit keyboard and relative mouse events through Win32 SendInput."""

    def press_key(self, scan_code):
        extra = ctypes.c_ulong(0)
        input_union = InputUnion()
        input_union.ki = KeyBdInput(
            0, scan_code, 0x0008, 0, ctypes.pointer(extra)
        )
        event = Input(ctypes.c_ulong(1), input_union)
        _send_input()(1, ctypes.pointer(event), ctypes.sizeof(event))

    def release_key(self, scan_code):
        extra = ctypes.c_ulong(0)
        input_union = InputUnion()
        input_union.ki = KeyBdInput(
            0, scan_code, 0x0008 | 0x0002, 0, ctypes.pointer(extra)
        )
        event = Input(ctypes.c_ulong(1), input_union)
        _send_input()(1, ctypes.pointer(event), ctypes.sizeof(event))

    def move_mouse(self, dx, dy):
        extra = ctypes.c_ulong(0)
        input_union = InputUnion()
        input_union.mi = MouseInput(
            dx=dx,
            dy=dy,
            mouseData=0,
            dwFlags=0x0001,
            time=0,
            dwExtraInfo=ctypes.pointer(extra),
        )
        event = Input(ctypes.c_ulong(0), input_union)
        _send_input()(1, ctypes.pointer(event), ctypes.sizeof(event))
