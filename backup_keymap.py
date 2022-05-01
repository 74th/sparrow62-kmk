from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard

layer1 = 0
layer2 = 1
layer3 = 2
layer4 = 3

____ = KC.TRANSPARENT

def layer1_keymap():
    left = [
        [KC.ESC,   KC.GRAVE,    KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [           KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6],
        [           KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC],
        [           KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC],
        [                       KC.LCTL,    KC.LGUI,    KC.LALT,    KC.SPC],
    ]
    right = [
        [                       KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [KC.F2,     KC.F3,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.EQL],
        [           KC.BSPC,    KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [           KC.ENT,     KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS],
        [           KC.RALT,    KC.RGUI,    KC.APP,     KC.BSPC],
    ]

    return [[left, right]]

def layer2_keymap():
    left = [
        [KC.ESC,   KC.GRAVE,    KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [           KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6],
        [           KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC],
        [           KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC],
        [                       KC.LCTL,    KC.LGUI,    KC.LALT,    KC.SPC],
    ]
    right = [
        [                       KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [KC.F2,     KC.F3,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.EQL],
        [           KC.BSPC,    KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [           KC.ENT,     KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS],
        [           KC.RALT,    KC.RGUI,    KC.APP,     KC.BSPC],
    ]

    return [[left, right]]

def layer3_keymap():
    left = [
        [KC.ESC,   KC.GRAVE,    KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [           KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6],
        [           KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC],
        [           KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC],
        [                       KC.LCTL,    KC.LGUI,    KC.LALT,    KC.SPC],
    ]
    right = [
        [                       KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [KC.F2,     KC.F3,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.EQL],
        [           KC.BSPC,    KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [           KC.ENT,     KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS],
        [           KC.RALT,    KC.RGUI,    KC.APP,     KC.BSPC],
    ]

    return [[left, right]]

def layer4_keymap():
    left = [
        [KC.ESC,   KC.GRAVE,    KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [           KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6],
        [           KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC],
        [           KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC],
        [                       KC.LCTL,    KC.LGUI,    KC.LALT,    KC.SPC],
    ]
    right = [
        [                       KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [KC.F2,     KC.F3,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.EQL],
        [           KC.BSPC,    KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [           KC.ENT,     KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS],
        [           KC.RALT,    KC.RGUI,    KC.APP,     KC.BSPC],
    ]

    return [[left, right]]

def layer5_keymap():
    left = [
        [KC.ESC,   KC.GRAVE,    KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [           KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6],
        [           KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC],
        [           KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC],
        [                       KC.LCTL,    KC.LGUI,    KC.LALT,    KC.SPC],
    ]
    right = [
        [                       KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [KC.F2,     KC.F3,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.EQL],
        [           KC.BSPC,    KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [           KC.ENT,     KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS],
        [           KC.RALT,    KC.RGUI,    KC.APP,     KC.BSPC],
    ]

    return [[left, right]]


def layer6_keymap():
    left = [
        [KC.ESC,   KC.GRAVE,    KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [           KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6],
        [           KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC],
        [           KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC],
        [                       KC.LCTL,    KC.LGUI,    KC.LALT,    KC.SPC],
    ]
    right = [
        [                       KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [KC.F2,     KC.F3,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.EQL],
        [           KC.BSPC,    KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [           KC.ENT,     KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS],
        [           KC.RALT,    KC.RGUI,    KC.APP,     KC.BSPC],
    ]

    return [[left, right]]

def get_keymap(keyboard: KMKKeyboard):
    layer1 = layer1_keymap()
    layer2 = layer2_keymap()
    layer3 = layer3_keymap()
    layer4 = layer4_keymap()
    layer5 = layer5_keymap()
    layer6 = layer6_keymap()
    return [layer1[0], layer2[0], layer3[0], layer4[0], layer5[0], layer6[0]]

def on_before_start(keyboard: KMKKeyboard):
    keyboard.pixels.set_rgb_fill((64, 0, 0))