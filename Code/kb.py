import board
import neopixel

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import MatrixScanner, DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()

        self.col_pins = (
            board.GP3,
            board.GP4,
            board.GP2
        )

        self.row_pins = (
            board.GP6,
            board.GP7,
            board.GP0
        )

        self.diode_orientation = DiodeOrientation.COL2ROW

        self.matrix = MatrixScanner(
            column_pins=self.col_pins,
            row_pins=self.row_pins,
            diode_orientation=self.diode_orientation
        )

        self.encoder_button_pin = board.GP28

        self.num_leds = 14

        self.leds = neopixel.NeoPixel(
            board.GP1,
            self.num_leds,
            brightness=0.5,
            auto_write=False,
            pixel_order=neopixel.GRBW
        )

        self.led_positions = [
            (11, 0.5),
            (2, 27.5),
            (2, 46.5),
            (2, 65.5),
            (20.475, 27.5),
            (20.475, 46.5),
            (20.475, 65.5),
            (39.525, 27.5),
            (39.525, 46.5),
            (39.525, 65.5),
            (58, 27.5),
            (58, 46.5),
            (58, 65.5),
            (49.25, 0.5)
        ]

    def led_startup(self):
        for i in range(self.num_leds):
            self.leds[i] = (255, 255, 255, 0)
            self.leds.show()

        for i in range(self.num_leds):
            self.leds[i] = (0, 0, 0, 0)

        self.leds.show()