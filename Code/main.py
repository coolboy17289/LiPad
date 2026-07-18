import board
import time
import math
import digitalio

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.rotary_encoder import RotaryEncoderHandler

from kb import KMKKeyboard


keyboard = KMKKeyboard()


layers = Layers()
keyboard.modules.append(layers)


keyboard.keymap = [
    [
        KC.MRWD,
        KC.MPLY,
        KC.MFFD
    ],

    [
        KC.MSEL,
        KC.CALC,
        KC.LGUI(KC.R)
    ],

    [
        KC.LEFT,
        KC.RIGHT,
        KC.LGUI(KC.L)
    ]
]


encoder = RotaryEncoderHandler()
keyboard.modules.append(encoder)


encoder.pins = (
    (board.GP26, board.GP27, None),
)

encoder.divisor = 4

encoder.map = [
    ((KC.VOLD, KC.VOLU),)
]


encoder_button = digitalio.DigitalInOut(
    board.GP28
)

encoder_button.switch_to_input(
    pull=digitalio.Pull.UP
)


modes = [
    "solid",
    "rainbow",
    "wave",
    "reactive",
    "idle"
]


mode = 0


layer_hues = {
    0: 190,
    1: 120,
    2: 280
}


last_activity = time.monotonic()
idle_time = 120

button_last = False
button_press = 0


def hsv(h, s, v):
    h %= 360

    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if h < 60:
        r, g, b = c, x, 0
    elif h < 120:
        r, g, b = x, c, 0
    elif h < 180:
        r, g, b = 0, c, x
    elif h < 240:
        r, g, b = 0, x, c
    elif h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return (
        int((r + m) * 255),
        int((g + m) * 255),
        int((b + m) * 255),
        0
    )


def next_mode():
    global mode

    mode = (
        mode + 1
    ) % len(modes)


def render_leds():
    t = time.monotonic()

    hue = layer_hues.get(
        keyboard.active_layers[0],
        200
    )

    current = modes[mode]

    for i, (x, y) in enumerate(
        keyboard.led_positions
    ):

        if current == "solid":

            value = (
                math.sin(t * 1.5) + 1
            ) / 2

            keyboard.leds[i] = hsv(
                hue,
                0.9,
                value
            )


        elif current == "rainbow":

            keyboard.leds[i] = hsv(
                x * 25 + y * 20 + t * 40,
                1,
                1
            )


        elif current == "wave":

            value = (
                math.sin(t * 2 + x + y) + 1
            ) / 2

            keyboard.leds[i] = hsv(
                hue + value * 70,
                0.8,
                value
            )


        elif current == "reactive":

            keyboard.leds[i] = hsv(
                hue,
                1,
                1
            )


        elif current == "idle":

            value = (
                math.sin(t * 0.5) + 1
            ) / 2

            keyboard.leds[i] = hsv(
                200,
                0.5,
                value * 0.25
            )


    keyboard.leds.show()


def check_idle():
    global mode

    if time.monotonic() - last_activity > idle_time:
        mode = len(modes) - 1


def check_button():
    global button_last
    global button_press
    global last_activity

    pressed = not encoder_button.value

    if pressed and not button_last:
        button_press = time.monotonic()

    if not pressed and button_last:

        duration = (
            time.monotonic()
            -
            button_press
        )

        if duration > 1:
            keyboard.active_layers[0] = (
                keyboard.active_layers[0] + 1
            ) % 3

        else:
            next_mode()

        last_activity = time.monotonic()

    button_last = pressed


def tick():
    check_idle()
    check_button()
    render_leds()


keyboard.before_matrix_scan.append(tick)


keyboard.go()