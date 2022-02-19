from kmk.keys import KC

base_mac = 0
linux = 0

base_mac_left = [
    [KC.ESC,    KC.GRV,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5],
    [           KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.N6],
    [           KC.LCTL,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.LBRC],
    [           KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.RBRC],
    [                                               KC.ESC,     KC.LGUI,    KC.LCTL,    KC.SPC],
]
base_mac_right = [
    [                       KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,    KC.EQL],
    [KC.F2,     KC.F3,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSLS],
    [           KC.BSPC,    KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT],
    [           KC.ENT,     KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.F12],
    [           KC.RALT,    KC.RGUI,    KC.RCTL,    KC.RCTL],
]

def get_keymap():
    return [
        [base_mac_left, base_mac_right]
    ]