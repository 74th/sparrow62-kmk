from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence
from secret import input_otp1, input_otp2, input_otp3
from kmk.kmk_keyboard import KMKKeyboard


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

def CG(kc):
    return KC.LCTL(KC.LGUI(kc))


linux_base_layer = 0
linux_raise_layer = 1
mac_base_layer = 2
mac_raise_layer = 3
special_layer = 4

ubuntu_orange = (2, 1, 0)
mac_blue = (0, 0, 1)
led_clear = (0, 0, 0)

____ = KC.TRANSPARENT

special = KC.MO(special_layer)

def linux_keymap(keyboard: KMKKeyboard):
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
        [                                               esc_eisu,   alt_tab,    ctl_eisu,   KC.SPC],
    ]
    # トラックパッド併用のため、右手内側 4 キーは使わない https://twitter.com/74th/status/1502902835629137922
    base_right = [
        [           KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [____,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.EQL],
        [____,      KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [____,      KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS],
        [____,      raise_ent,  gui_kana,   KC.BSPC],
    ]
    raise_left = [
        [____,      CA(KC.F2),  G(KC.F1),   SG(KC.F2),  G(KC.F3),   SG(KC.F2),  CA(KC.ESC)],
        [           KC.ESC,     KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.F6],
        [           KC.GRV,     S(KC.N1),   S(KC.N2),   S(KC.N3),   S(KC.N4),   S(KC.N5),   S(KC.N6)],
        [           KC.LSHIFT,  ____,       ____,       pr_window,  pr_screen,  KC.F12,     ____],
        [                                               KC.ESC,     KC.LALT,    KC.LCTL,    KC.MINS],
    ]
    raise_right = [
        [           G(KC.F6),   G(KC.F7),   G(KC.F8),   G(KC.F9),   ____,       ____],
        [____,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12],
        [____,      S(KC.N7),   S(KC.N8),   S(KC.N9),   S(KC.N0),   S(KC.MINS), KC.EQL],
        [____,      KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   KC.HOME,    KC.END],
        [____,      ____,       ____,       KC.DEL],
    ]
    return [[base_left, base_right], [raise_left,raise_right]]

def mac_keymap(keyboard: KMKKeyboard):
    eisu = KC.LANG2
    kana = KC.LANG1
    pr_window = SG(KC.N3)
    pr_screen = SG(KC.N4)

    ctl_tab = KC.MT(KC.TAB, KC.LCTRL, prefer_hold=True)
    opt_tab = KC.MT(KC.TAB, KC.LALT, prefer_hold=True)
    cmd_eisu = KC.MT(eisu, KC.LGUI, prefer_hold=True)
    opt_kana = KC.MT(kana, KC.LALT, prefer_hold=True)
    esc_eisu = simple_key_sequence([eisu, KC.ESC])
    raise_ent = KC.LT(mac_raise_layer, KC.ENT, prefer_hold=True)

    base_left = [
        [special,   KC.GRAVE,   KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
        [           KC.GRAVE,   KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6],
        [           ctl_tab,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC],
        [           KC.LSHIFT,  KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC],
        [                                               esc_eisu,   opt_tab,    cmd_eisu,   KC.SPC],
    ]
    base_right = [
        [           KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
        [____,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.EQL],
        [____,      KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
        [____,      KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS],
        [____,      raise_ent,  opt_kana,   KC.BSPC],
    ]

    raise_left = [
        [____,      CA(KC.Q),   G(KC.F1),   CA(KC.F2),  G(KC.F3),   G(KC.F4),   CA(KC.ESC)],
        [           KC.ESC,     KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.F6],
        [           KC.LCTL,    S(KC.N1),   S(KC.N2),   S(KC.N3),   S(KC.N4),   S(KC.N5),   S(KC.N6)],
        [           KC.LSHIFT,  ____,       ____,       pr_window,  pr_screen,  KC.F12,     ____],
        [                       esc_eisu,   KC.SPC,     KC.LGUI,    KC.MINS],
    ]
    raise_right = [
        [           G(KC.F6),   G(KC.F7),   G(KC.F8),   G(KC.F9),   ____,       ____],
        [____,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12],
        [____,      S(KC.N7),   S(KC.N8),   S(KC.N9),   S(KC.N0),   S(KC.MINS), KC.EQL],
        [____,      KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   KC.HOME,    KC.END],
        [____,      ____,       ____,       KC.DEL],
    ]
    return [[base_left, base_right], [raise_left, raise_right]]


def special_keymap(keyboard: KMKKeyboard):
    to_mac = KC.DF(mac_base_layer)
    to_mac.after_press_handler(lambda *args: keyboard.pixels.set_rgb_fill(mac_blue))
    to_linux = KC.DF(linux_base_layer)
    to_linux.after_press_handler(lambda *args: keyboard.pixels.set_rgb_fill(ubuntu_orange))
    def do_soft_reset(*args):
        keyboard.pixels.set_rgb_fill(led_clear)
        import supervisor
        supervisor.reload()
    reset = KC.NO.clone()
    reset.after_press_handler(do_soft_reset)


    raise_left = [
        [____,      ____,       to_mac,     to_linux,   ____,       ____,       ____],
        [           ____,       reset,      ____,       ____,       ____,       ____,       ____],
        [           KC.CAPS,    input_otp3,       ____,       ____,       ____,       ____,       ____],
        [           ____,       input_otp1, input_otp2, ____,       ____,       ____,       ____],
        [                                               ____,       ____,       ____,       ____],
    ]
    raise_right = [
        [           ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____,       ____,       ____,       ____],
        [____,      ____,       ____,       ____],
    ]
    return [raise_left, raise_right]

def get_keymap(keyboard: KMKKeyboard):
    linux_base, linux_raise = linux_keymap(keyboard)
    mac_base, mac_raise = mac_keymap(keyboard)
    return [
        linux_base,
        linux_raise,
        mac_base,
        mac_raise,
        special_keymap(keyboard),
    ]

def on_before_start(keyboard: KMKKeyboard):
    keyboard.pixels.set_rgb_fill(ubuntu_orange)
