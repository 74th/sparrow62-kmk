from adafruit_mcp230xx.mcp23017 import MCP23017
import board
import busio
import digitalio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
modtap = ModTap()
keyboard.modules.append(modtap)

from keymap import get_keymap

i2c = busio.I2C(board.GP13, board.GP12, frequency=300_000)
mcp = MCP23017(i2c)


def get_wrapper_class():
    class DigitalInOut:
        def __init__(
            self,
            base,
        ):
            self.base = base

        def switch_to_input(self, pull):
            # skip pull-down register
            self.base.switch_to_input()

        def switch_to_output(self):
            self.base.switch_to_output()

        def get_value(self):
            return self.base.value

        def set_value(self, value):
            self.base.value = value

        value = property(get_value, set_value)

    return DigitalInOut

def get_dual_output_class():
    class DigitalInOut:
        def __init__(
            self,
            base1,
            base2,
        ):
            if base1.__class__.__name__ == 'DigitalInOut':
                self.base1 = base1
            else:
                self.base1 = digitalio.DigitalInOut(base1)
            if base2.__class__.__name__ == 'DigitalInOut':
                self.base2 = base2
            else:
                self.base2 = digitalio.DigitalInOut(base2)

        def switch_to_input(self, pull):
            raise Exception("no input")

        def switch_to_output(self):
            self.base1.switch_to_output()
            self.base2.switch_to_output()

        def get_value(self):
            raise Exception("no input")

        def set_value(self, value):
            self.base1.value = value
            self.base2.value = value

        value = property(get_value, set_value)

    return DigitalInOut


WrappedDigitalInOut = get_wrapper_class()
DualDigitalOut = get_dual_output_class()

keyboard.col_pins = [
    DualDigitalOut(board.GP5, mcp.get_pin(8)),
    DualDigitalOut(board.GP6, mcp.get_pin(9)),
    DualDigitalOut(board.GP7, mcp.get_pin(10)),
    DualDigitalOut(board.GP8, mcp.get_pin(11)),
    DualDigitalOut(board.GP9, mcp.get_pin(12)),
    DualDigitalOut(board.GP10, mcp.get_pin(13)),
    DualDigitalOut(board.GP11, mcp.get_pin(14)),
]
mcp.iodirb = 0

keyboard.row_pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    WrappedDigitalInOut(mcp.get_pin(0)),
    WrappedDigitalInOut(mcp.get_pin(1)),
    WrappedDigitalInOut(mcp.get_pin(2)),
    WrappedDigitalInOut(mcp.get_pin(3)),
    WrappedDigitalInOut(mcp.get_pin(4)),
]
mcp.iodira = 1
n_rows = len(keyboard.row_pins)
n_cols = len(keyboard.col_pins)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

left_map = [
    [(0,0),     (0,1),      (1,0),      (2,0),      (3,0),      (4,0),      (5,0)],
    [           (0,2),      (1,1),      (2,1),      (3,1),      (4,1),      (5,1),      (6,1)],
    [           (0,3),      (1,2),      (2,2),      (3,2),      (4,2),      (5,2),      (6,2)],
    [           (0,4),      (1,3),      (2,3),      (3,3),      (4,3),      (5,3),      (6,3)],
    [                                               (3,4),      (4,4),      (5,4),      (6,4)],
]
right_map = [
    [                       (1,5),      (2,5),      (3,5),      (4,5),      (5,5),      (6,5)],
    [(0,5),     (0,6),      (1,6),      (2,6),      (3,6),      (4,6),      (5,6),      (6,6)],
    [           (0,7),      (1,7),      (2,7),      (3,7),      (4,7),      (5,7),      (6,7)],
    [           (0,8),      (1,8),      (2,8),      (3,8),      (4,8),      (5,8),      (6,8)],
    [           (0,9),      (1,9),      (2,9),      (3,9)],
]

def apply_to_map(
    keys: list[list[int]], keymap: list[list[tuple[int, int]]], to: list[int]
):
    for row_no, rows in enumerate(keymap):
        for col_no, _ in enumerate(rows):
            pos = keymap[row_no][col_no]
            to[pos[0] + pos[1] * n_cols] = keys[row_no][col_no]


layers = get_keymap()
keyboard.keymap = []

for n, layer in enumerate(layers):
    keymap = [KC.NO] * len(keyboard.col_pins) * len(keyboard.row_pins)
    apply_to_map(layer[0], left_map, keymap)
    apply_to_map(layer[1], right_map, keymap)
    keyboard.keymap.append(keymap)


# keyboard.keymap = [[]]
# keyboard.debug_enabled = True

if __name__ == "__main__":
    keyboard.go()
    pass
