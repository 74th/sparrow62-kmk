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


def main():
    try:
        from kmk.kmk_keyboard import KMKKeyboard
        from kmk.keys import KC
        from kmk.scanners import DiodeOrientation
        from kmk.scanners.digitalio import MatrixScanner
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

    keyboard = KMKKeyboard()
    keyboard.modules.append(Layers())
    modtap = ModTap()
    keyboard.modules.append(modtap)

    led_ext = RGB(board.GP18, 1, val_default=6)
    led_ext.set_rgb_fill((255, 255, 255))

    keyboard.pixels = led_ext
    keyboard.pixels.set_rgb_fill((255, 255, 255))

    keyboard.col_pins = [
        board.GP25,
        board.GP24,
        board.GP23,
        board.GP22,
        board.GP21,
        board.GP20,
        board.GP19,
        board.GP17,
        board.GP16,
        board.GP14,
        board.GP13,
        board.GP12,
        board.GP11,
    ]

    keyboard.row_pins = [
        board.A3,
        board.GP28,
        board.GP27,
        board.GP26,
        board.GP15,
    ]
    n_rows = len(keyboard.row_pins)
    n_cols = len(keyboard.col_pins)

    keyboard.diode_orientation = DiodeOrientation.COL2ROW

    key_assign_map = [
        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),         (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0),],
        [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1),],
        [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2),],
        [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3),],
        [                        (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4),          (11, 4),],
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

        import sparrow59_keymap as keymap_mod

        layers = keymap_mod.get_keymap(keyboard)
        keyboard.keymap = []

        for _, layer in enumerate(layers):
            keymap = [KC.NO] * len(keyboard.col_pins) * len(keyboard.row_pins)
            apply_to_map(layer, key_assign_map, keymap)
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

        import sparrow59_keymap as backup_keymap_mod

        layers = backup_keymap_mod.get_keymap(keyboard)
        keyboard.keymap = []

        for _, layer in enumerate(layers):
            keymap = [KC.NO] * len(keyboard.col_pins) * len(keyboard.row_pins)
            apply_to_map(layer, left_map, keymap)
            keyboard.keymap.append(keymap)

        if hasattr(backup_keymap_mod, "on_before_start"):
            backup_keymap_mod.on_before_start(keyboard)

        print("start keyboard")

    keyboard.matrix = MatrixScanner( # type:ignore
        cols=keyboard.col_pins,
        rows=keyboard.row_pins,
        diode_orientation=keyboard.diode_orientation,
    )

    keyboard.go()


if __name__ == "__main__":
    main()
