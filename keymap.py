from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence, send_string
from secret import input_otp1, input_otp2


def S(kc):
    return KC.LSFT(kc)

def C(kc):
    return KC.LCTL(kc)

def A(kc):
    return KC.LALT(kc)

def G(kc):
    return KC.LGUI(kc)

def CA(kc):
    return KC.LCTL(KC.LALT(kc))

def SG(kc):
    return KC.LSFT(KC.LGUI(kc))


mac_base_layer = 0
mac_raise_layer = 1
linux_base_layer = 2
linux_raise_layer = 3
special_layer = 4


____ = KC.TRANSPARENT

special = KC.MO(special_layer)

def mac_keymap():
    eisu = KC.LANG2
    kana = KC.LANG1
    pr_window = SG(KC.N3)
    pr_screen = SG(KC.N4)

    ctl_tab = KC.MT(KC.TAB, KC.LCTRL, prefer_hold=True)
    cmd_eisu = KC.MT(eisu, KC.LGUI, prefer_hold=True)
    opt_kana = KC.MT(kana, KC.LALT, prefer_hold=True)
    esc_eisu = simple_key_sequence([eisu, KC.ESC])
    raise_ent = KC.LT(mac_raise_layer, KC.ENT, prefer_hold=True)

    base_left = [
        [special,   KC.GRAVE,   KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [           KC.GRAVE,   KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6],
        [           ctl_tab,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC],
        [           KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC],
        [                       esc_eisu,   ctl_tab,    cmd_eisu,   KC.SPC],
    ]
    base_right = [
        [                       KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [KC.F2,     KC.F3,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.EQL],
        [           KC.BSPC,    KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [           KC.ENT,     KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS],
        [           KC.ENTER,   raise_ent,  opt_kana,   KC.BSPC],
    ]

    raise_left = [
        [____,      CA(KC.Q),   G(KC.F1),   SG(KC.F2),  G(KC.F3),   G(KC.F4),   CA(KC.ESC)],
        [           KC.ESC,     KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.F6],
        [           KC.LCTL,    S(KC.N1),   S(KC.N2),   S(KC.N3),   S(KC.N4),   S(KC.N5),   S(KC.N6)],
        [           KC.LSHIFT,  ____,       ____,       pr_window,  pr_screen,  KC.F12,     ____],
        [                       esc_eisu,   KC.SPC,     KC.LGUI,    KC.MINS],
    ]
    raise_right = [
        [                       G(KC.F6),   G(KC.F7),   G(KC.F8),   G(KC.F9),   ____,       ____],
        [KC.F2,     KC.F3,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12],
        [           ____,       S(KC.N7),   S(KC.N8),   S(KC.N9),   S(KC.N0),   S(KC.MINS), KC.EQL],
        [           ____,       KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   KC.HOME,    KC.END],
        [           ____,       ____,       ____,       KC.DEL],
    ]
    return [[base_left, base_right], [raise_left, raise_right]]

def linux_keymap():
    eisu = KC.MHEN
    kana = KC.HENK
    pr_window = A(KC.PSCREEN)
    pr_screen = S(KC.PSCREEN)

    alt_tab = KC.MT(KC.TAB, KC.LALT, prefer_hold=True)
    ctl_tab = KC.MT(KC.TAB, KC.LCTRL, prefer_hold=True)
    ctl_eisu = KC.MT(eisu, KC.LCTRL, prefer_hold=True)
    gui_kana = KC.MT(kana, KC.LGUI, prefer_hold=True)
    esc_eisu = simple_key_sequence([eisu, KC.ESC])
    raise_ent = KC.LT(linux_raise_layer, KC.ENT, prefer_hold=True)

    base_left = [
        [special,   KC.GRAVE,   KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [           KC.GRAVE,   KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6],
        [           ctl_tab,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC],
        [           KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC],
        [                       esc_eisu,   alt_tab,    ctl_eisu,   KC.SPC],
    ]
    base_right = [
        [                       KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [KC.F2,     KC.F3,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.EQL],
        [           KC.BSPC,    KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [           KC.ENT,     KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS],
        [           KC.ENTER,   raise_ent,  gui_kana,   KC.BSPC],
    ]
    raise_left = [
        [____,      CA(KC.F2),  G(KC.F1),   SG(KC.F2),  G(KC.F3),   G(KC.F4),   CA(KC.ESC)],
        [           KC.ESC,     KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.F6],
        [           KC.GRV,     S(KC.N1),   S(KC.N2),   S(KC.N3),   S(KC.N4),   S(KC.N5),   S(KC.N6)],
        [           KC.LSHIFT,  ____,       ____,       pr_window,  pr_screen,  KC.F12,     ____],
        [                       KC.ESC,     KC.LALT,    KC.LCTL,     KC.MINS],
    ]
    raise_right = [
        [                       G(KC.F6),   G(KC.F7),   G(KC.F8),   G(KC.F9),   ____,       ____],
        [KC.F2,     KC.F3,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12],
        [           ____,       S(KC.N7),   S(KC.N8),   S(KC.N9),   S(KC.N0),   S(KC.MINS), KC.EQL],
        [           ____,       KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   KC.HOME,    KC.END],
        [           ____,       ____,       ____,       KC.DEL],
    ]
    return [[base_left, base_right], [raise_left,raise_right]]

def special_keymap():
    to_mac = KC.DF(mac_base_layer)
    to_linux = KC.DF(linux_base_layer)

    raise_left = [
        [____,      ____,       to_mac,     to_linux,   ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       input_otp2, input_otp1, ____,       ____,       ____,       ____],
        [                       ____,       ____,       ____,       ____],
    ]
    raise_right = [
        [                       ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____,       ____,       ____,       ____],
        [           ____,       ____,       ____,       ____],
    ]
    return [raise_left,raise_right]

def get_keymap():
    mac_base, mac_raise = mac_keymap()
    linux_base, linux_raise = linux_keymap()
    return [
        mac_base,
        mac_raise,
        linux_base,
        linux_raise,
        special_keymap(),
    ]
