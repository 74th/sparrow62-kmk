from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard

layer1 = 0
layer2 = 1
layer3 = 2
layer4 = 3
layer5 = 4
layer6 = 5

____ = KC.TRANSPARENT

mo_layer2 = KC.MO(layer2)
mo_layer3 = KC.MO(layer3)
mo_layer4 = KC.MO(layer4)
mo_layer5 = KC.MO(layer5)
mo_layer6 = KC.MO(layer6)

def layer1_keymap(keyboard: KMKKeyboard):
    return [
        [KC.GRAVE,   KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,                KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6,    KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSLS],
        [KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC,  KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC,  KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.ENT],
        [                                    KC.LCTL,    KC.LGUI,    KC.LALT,    KC.SPC,   KC.RGUI,    KC.RCTL,    KC.BSPC,                KC.ENT],
    ]

def get_keymap(keyboard: KMKKeyboard):
    layer1 = layer1_keymap(keyboard)
    return [layer1]

def on_before_start(keyboard: KMKKeyboard):
    keyboard.pixels.set_rgb_fill((2, 2, 2))
