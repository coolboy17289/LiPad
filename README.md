# LiPad

# Features

## Hardware

- Custom-designed PCB
- Compact macropad layout
- RP2040-based controller support
- Mechanical key switches
- Rotary encoder with push button
- 14x SK6812 MINI addressable RGB LEDs
- Custom LED positioning for animations
- Designed using KiCad

## Firmware

LiPad uses:

- CircuitPython
- KMK Firmware
- NeoPixel RGB control

Current firmware features:

- Programmable key layers
- Media controls
- Rotary encoder volume control
- Encoder button actions
- RGB lighting effects
- Idle lighting mode
- Custom keyboard matrix support

---

# Project Structure

```
LiPad/
├── PCB/
│   ├── KiCad schematic files
│   ├── PCB layout files
│   └── 3D model files
│
├── Code/
│   ├── main.py
│   ├── kb.py
│   ├── code.py
│   └── requirements.txt
│
├── README.md
├── .gitignore
└── .vscode/
    └── settings.json
```

---

# Firmware

The LiPad firmware is separated into hardware configuration and keyboard behaviour.

## code.py

`code.py` is the CircuitPython startup file.

When the controller powers on, CircuitPython automatically runs this file to start the keyboard firmware.

---

## main.py

`main.py` contains the main functionality of LiPad.

It controls:

- Keyboard keymaps
- Layers
- Rotary encoder functions
- Encoder button behaviour
- RGB lighting effects
- Idle detection
- Keyboard events

The main firmware logic is designed to be easy to edit and customise without changing the hardware configuration.

---

## kb.py

`kb.py` defines the physical hardware of LiPad.

It contains:

- Matrix row pins
- Matrix column pins
- Diode orientation
- LED configuration
- LED count
- LED physical positions

This separation allows the firmware logic to change without needing to rewrite the hardware setup.

---

# Keyboard Layers

LiPad currently includes three layers.

## Layer 0 - Main

Default controls:

| Key | Function |
|---|---|
| Key 1 | Previous track |
| Key 2 | Play/Pause |
| Key 3 | Next track |

---

## Layer 1 - Utility

Additional shortcuts:

| Key | Function |
|---|---|
| Key 1 | Media select |
| Key 2 | Calculator |
| Key 3 | Windows Run |



# RGB Lighting

LiPad uses 14 SK6812 MINI addressable RGB LEDs.

The firmware supports multiple lighting modes:

## Solid

A breathing effect using the active layer colour.

## Rainbow

A moving rainbow animation across the LED layout.

## Wave

A wave animation based on the LED positions.

## Reactive

A bright reactive lighting mode.

## Idle

A low-power animation used when the keyboard has not been used for a period of time.



# PCB Design

The PCB for LiPad was designed using KiCad.

The PCB directory contains:

- Schematic files
- PCB layout
- Component footprints
- 3D model exports
- Design reports

The design was created with custom placement and routing to support the LiPad layout.



# Development

## Requirements

Development requires:

- Linux, Windows, or macOS
- Python 3
- Git
- VS Code recommended
- CircuitPython compatible controller

## Installing Development Tools

Navigate to the firmware folder:

```bash
cd Code
```

Install requirements:

```bash
python3 -m pip install -r requirements.txt
```



# Building Firmware

After preparing the CircuitPython controller:

1. Connect the board through USB
2. Enter bootloader mode
3. Copy the firmware files to the `CIRCUITPY` drive

Required files:

```
CIRCUITPY/
├── code.py
├── main.py
├── kb.py
└── lib/
```



# Future Plans

Possible future improvements:

- [ ] Custom LiPad case
- [ ] OLED display support
- [ ] More programmable layers
- [ ] Configuration software
- [ ] VIA/Vial compatibility
- [ ] Wireless support
- [ ] Improved RGB effects
- [ ] Build documentation
- [ ] Manufacturing files



# Contributing

Contributions are welcome.

If you would like to improve LiPad:

1. Fork the repository
2. Create a new branch



# License

LiPad is an open-source hardware and firmware project.

License information will be added before the first official release.



# Author

Created by **Lihan Badenhorst**

Project: **LiPad**
