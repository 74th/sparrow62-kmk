from keymap import get_keymap as get_keymap62
from keymap import on_before_start
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

def keymap_convert(sparrow62: list[list[list]]):
    l, r = sparrow62
    return [
        [l[0][0],   l[0][2],    l[0][3],    l[0][4],    l[0][5],    l[0][6],                r[0][0],    r[0][1],    r[0][2],    r[0][3],    r[0][4],    r[0][5]],
        [l[1][0],   l[1][1],    l[1][2],    l[1][3],    l[1][4],    l[1][5],    l[1][6],    r[1][1],    r[1][2],    r[1][3],    r[1][4],    r[1][5],    r[1][6]],
        [l[2][0],   l[2][1],    l[2][2],    l[2][3],    l[2][4],    l[2][5],    l[2][6],    r[2][1],    r[2][2],    r[2][3],    r[2][4],    r[2][5],    r[2][6]],
        [l[3][0],   l[3][1],    l[3][2],    l[3][3],    l[3][4],    l[3][5],    l[3][6],    r[3][1],    r[3][2],    r[3][3],    r[3][4],    r[3][5],    r[3][6]],
        [                                   l[4][0],    l[4][1],    l[4][2],    l[4][3],    r[4][1],    r[4][2],    r[4][3],                l[0][1]],
    ]

def get_keymap(keyboard: KMKKeyboard):
    layers = get_keymap62(keyboard)
    return [keymap_convert(layer) for layer in layers]
