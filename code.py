import supervisor
import traceback
import board
import busio
import time
import digitalio


def reboot_with_error(message: list[str], exp: Exception):
    for i in range(10):
        print()
        traceback.print_exception(None, exp, exp.__traceback__)
        print()
        for m in message:
            print(m)
        print()
        print(f"auto reload after {10-i} sec")
        print()
        time.sleep(1)
    supervisor.reload()


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
            if base1.__class__.__name__ == "DigitalInOut":
                self.base1 = base1
            else:
                self.base1 = digitalio.DigitalInOut(base1)
            if base2.__class__.__name__ == "DigitalInOut":
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


def main():
    try:
        from adafruit_mcp230xx.mcp23017 import MCP23017
    except ImportError as e:
        reboot_with_error(["cannot find adfruit_mcp230xx module"], e)
        return

    try:
        from kmk.kmk_keyboard import KMKKeyboard
        from kmk.keys import KC
        from kmk.matrix import DiodeOrientation
        from kmk.modules.layers import Layers
        from kmk.modules.modtap import ModTap
        from kmk.extensions.rgb import RGB
    except ImportError as e:
        reboot_with_error(["cannot find kmk module"], e)
        return
    try:
        import neopixel
    except ImportError as e:
        reboot_with_error(["cannot find neopixel module"], e)
        return

    try:
        i2c = busio.I2C(board.GP13, board.GP12, frequency=300_000)
        mcp = MCP23017(i2c)
    except ValueError as e:
        reboot_with_error(["cannot communicate to right board."], e)
        return
    except RuntimeError as e:
        reboot_with_error(["cannot communicate to right board."], e)
        return

    keyboard = KMKKeyboard()
    keyboard.modules.append(Layers())
    modtap = ModTap()
    keyboard.modules.append(modtap)

    led_ext = RGB(board.GP14, 1, val_default=6)
    led_ext.set_rgb_fill((255, 255, 255))

    keyboard.pixels = led_ext
    keyboard.pixels.set_rgb_fill((255, 255, 255))

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
        [(0, 0), (0, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)],
        [(0, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)],
        [(0, 3), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2)],
        [(0, 4), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3)],
        [(3, 4), (4, 4), (5, 4), (6, 4)],
    ]
    right_map = [
        [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)],
        [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)],
        [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7)],
        [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8)],
        [(0, 9), (1, 9), (2, 9), (3, 9)],
    ]

    def apply_to_map(
        keys: list[list[int]], keymap: list[list[tuple[int, int]]], to: list[int]
    ):
        col_no = -1
        row_no = -1
        for row_no, rows in enumerate(keymap):
            for col_no, _ in enumerate(rows):
                pos = None
                try:
                    pos = keymap[row_no][col_no]
                    to[pos[0] + pos[1] * n_cols] = keys[row_no][col_no]
                except IndexError as e:
                    raise Exception(f"check your keymap row:{row_no}, col:{col_no}")


    try:
        print("load keymap")

        import keymap as keymap_mod

        layers = keymap_mod.get_keymap(keyboard)
        keyboard.keymap = []

        for _, layer in enumerate(layers):
            keymap = [KC.NO] * len(keyboard.col_pins) * len(keyboard.row_pins)
            apply_to_map(layer[0], left_map, keymap)
            apply_to_map(layer[1], right_map, keymap)
            keyboard.keymap.append(keymap)

        if hasattr(keymap_mod, "on_before_start"):
            keymap_mod.on_before_start(keyboard)

        print("start keyboard")

    except Exception as e:
        print()
        print("keymap has error")
        print()
        traceback.print_exception(None, e, e.__traceback__)
        print()
        print("load backup keymap")
        print()
        keyboard.pixels.set_rgb_fill((255, 0, 0))

        import backup_keymap as backup_keymap_mod

        layers = backup_keymap_mod.get_keymap(keyboard)
        keyboard.keymap = []

        for _, layer in enumerate(layers):
            keymap = [KC.NO] * len(keyboard.col_pins) * len(keyboard.row_pins)
            apply_to_map(layer[0], left_map, keymap)
            apply_to_map(layer[1], right_map, keymap)
            keyboard.keymap.append(keymap)

        if hasattr(backup_keymap_mod, "on_before_start"):
            backup_keymap_mod.on_before_start(keyboard)

        print("start keyboard")

    keyboard.go()


if __name__ == "__main__":
    main()
