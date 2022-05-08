from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard

layer1 = 0

____ = KC.TRANSPARENT

def layer1_keymap(keyboard: KMKKeyboard):
    left = [
        [KC.ESC,    KC.GRAVE,   KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [           KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6],
        [           KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC],
        [           KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC],
        [                                               KC.LCTL,    KC.LGUI,    KC.LALT,    KC.SPC],
    ]
    right = [
        [           KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [KC.BSPC,   KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSLS],
        [KC.ENTER,  KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [KC.RSFT,   KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.RSFT],
        [KC.RALT,   KC.RGUI,    KC.RALT,    KC.RCTL],
    ]

    return [[left, right]]

def get_keymap(keyboard: KMKKeyboard):
    layer1 = layer1_keymap(keyboard)
    return [layer1[0]]

def on_before_start(keyboard: KMKKeyboard):
    keyboard.pixels.set_rgb_fill((0, 0, 64))
