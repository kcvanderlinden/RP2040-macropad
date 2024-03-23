import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

keyboard.col_pins = (board.GP8,)
keyboard.row_pins = (board.GP10, board.GP11, board.GP12, board.GP13,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.GP26, board.GP15, None, False),)
keyboard.tap_time = 250
keyboard.debug_enabled = False

# Layers
LYR_STD, LYR_EXT, LYR_NUM, LYR_GAME = 0, 1, 2, 3

keyboard.keymap = [
    [KC.A,KC.B,KC.C,KC.D,]
]

# Rotary Encoder (1 encoder / 1 definition per layer)
encoder_handler.map = [ ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN),), 
                        ]
if __name__ == '__main__':
    keyboard.go()