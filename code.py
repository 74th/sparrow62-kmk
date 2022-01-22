print("Starting")

from digitalio import DigitalInOut
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017
import board
import time
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()
i2c = busio.I2C(board.GP13, board.GP12)
mcp = MCP23017(i2c)



keyboard.col_pins = (
    DigitalInOut(board.GP0),
    DigitalInOut(board.GP1),
    DigitalInOut(board.GP2),
    DigitalInOut(board.GP3),
    DigitalInOut(board.GP4),
    DigitalInOut(board.GP5),
    DigitalInOut(board.GP6),
    mcp.get_pin(0),
    mcp.get_pin(1),
    mcp.get_pin(2),
    mcp.get_pin(3),
    mcp.get_pin(4),
    mcp.get_pin(5),
    mcp.get_pin(6),
)
keyboard.col_pins[0].switch_to_output()
keyboard.col_pins[1].switch_to_output()
keyboard.col_pins[2].switch_to_output()
keyboard.col_pins[3].switch_to_output()
keyboard.col_pins[4].switch_to_output()
keyboard.col_pins[5].switch_to_output()
keyboard.col_pins[6].switch_to_output()
mcp.iodira = 0

keyboard.row_pins = (
    DigitalInOut(board.GP7),
    DigitalInOut(board.GP8),
    DigitalInOut(board.GP9),
    DigitalInOut(board.GP10),
    DigitalInOut(board.GP11),
    mcp.get_pin(8),
    mcp.get_pin(9),
    mcp.get_pin(10),
    mcp.get_pin(11),
    mcp.get_pin(12),
    )
keyboard.row_pins[0].switch_to_input(pull=digitalio.Pull.DOWN)
keyboard.row_pins[0].switch_to_input(pull=digitalio.Pull.DOWN)
keyboard.row_pins[0].switch_to_input(pull=digitalio.Pull.DOWN)
keyboard.row_pins[0].switch_to_input(pull=digitalio.Pull.DOWN)
keyboard.row_pins[0].switch_to_input(pull=digitalio.Pull.DOWN)
mcp.iodirb = 1

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
        KC.A,
    ]
]

if __name__ == "__main__":
    keyboard.go()
