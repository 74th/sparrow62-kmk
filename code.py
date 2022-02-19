from adafruit_mcp230xx.mcp23017 import MCP23017
import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers

from keymap import get_keymap

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

i2c = busio.I2C(board.GP13, board.GP12)
mcp = MCP23017(i2c)


def get_wrapper_class():
    class DigitalInOut:
        def __init__(
            self,
            base,
        ):
            self.base = base

        def switch_to_input(self, pull):
            self.base.switch_to_input()

        def switch_to_output(self):
            self.base.switch_to_output()

        def get_value(self):
            return self.base.value

        def set_value(self, value):
            self.base.value = value

        value = property(get_value, set_value)

    return DigitalInOut


MCP23017DigitalInOutWrapper = get_wrapper_class()

keyboard.col_pins = [
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    MCP23017DigitalInOutWrapper(mcp.get_pin(8)),
    MCP23017DigitalInOutWrapper(mcp.get_pin(9)),
    MCP23017DigitalInOutWrapper(mcp.get_pin(10)),
    MCP23017DigitalInOutWrapper(mcp.get_pin(11)),
    MCP23017DigitalInOutWrapper(mcp.get_pin(12)),
    MCP23017DigitalInOutWrapper(mcp.get_pin(13)),
    MCP23017DigitalInOutWrapper(mcp.get_pin(14)),
]
mcp.iodirb = 0

keyboard.row_pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    MCP23017DigitalInOutWrapper(mcp.get_pin(0)),
    MCP23017DigitalInOutWrapper(mcp.get_pin(1)),
    MCP23017DigitalInOutWrapper(mcp.get_pin(2)),
    MCP23017DigitalInOutWrapper(mcp.get_pin(3)),
    MCP23017DigitalInOutWrapper(mcp.get_pin(4)),
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
    [                       (8,5),      (9,5),      (10,5),     (11,5),     (12,5),     (13,5)],
    [(7,5),     (7,6),      (8,6),      (9,6),      (10,6),     (11,6),     (12,6),     (13,6)],
    [           (7,7),      (8,7),      (9,7),      (10,7),     (11,7),     (12,7),     (13,7)],
    [           (7,8),      (8,8),      (9,8),      (10,8),     (11,8),     (12,8),     (13,8)],
    [           (7,9),      (8,9),      (9,9),      (10,9)],
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
