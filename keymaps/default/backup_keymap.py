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
        [KC.ENT,    KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [KC.RSFT,   KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    mo_layer2],
        [KC.RALT,   KC.RGUI,    KC.RCTL,    mo_layer2],
    ]

    return [[left, right]]

def layer2_keymap(keyboard: KMKKeyboard):
    left = [
        [____,      ____,       KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5],
        [           ____,       ____,       ____,       ____,       ____,       ____,       KC.F6],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [                                               ____,       ____,       ____,       ____],
    ]
    right = [
        [           KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   KC.HOME,    KC.END],
        [____,      KC.RGUI,    KC.APP,     KC.BSPC],
    ]

    return [[left, right]]

def layer3_keymap(keyboard: KMKKeyboard):
    left = [
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [                                               ____,       ____,       ____,       ____],
    ]
    right = [
        [           ____,       ____,       ____,       ____,      ____,        ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____],
    ]


    return [[left, right]]

def layer4_keymap(keyboard: KMKKeyboard):
    left = [
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [                                               ____,       ____,       ____,       ____],
    ]
    right = [
        [           ____,       ____,       ____,       ____,      ____,        ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____],
    ]

    return [[left, right]]

def layer5_keymap(keyboard: KMKKeyboard):
    left = [
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [                                               ____,       ____,       ____,       ____],
    ]
    right = [
        [           ____,       ____,       ____,       ____,      ____,        ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____],
    ]

    return [[left, right]]


def layer6_keymap(keyboard: KMKKeyboard):
    left = [
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [                                               ____,       ____,       ____,       ____],
    ]
    right = [
        [           ____,       ____,       ____,       ____,      ____,        ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____],
    ]

    return [[left, right]]

def get_keymap(keyboard: KMKKeyboard):
    layer1 = layer1_keymap(keyboard)
    layer2 = layer2_keymap(keyboard)
    layer3 = layer3_keymap(keyboard)
    layer4 = layer4_keymap(keyboard)
    layer5 = layer5_keymap(keyboard)
    layer6 = layer6_keymap(keyboard)
    return [layer1[0], layer2[0], layer3[0], layer4[0], layer5[0], layer6[0]]

def on_before_start(keyboard: KMKKeyboard):
    keyboard.pixels.set_rgb_fill((2, 2, 2))
