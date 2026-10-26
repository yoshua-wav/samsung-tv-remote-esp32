# ESP32 Samsung TV Remote

A custom hardware sidequest: building a physical remote control for a Samsung TV using an ESP32 microcontroller and MicroPython. 

## Hardware Setup
- ESP32 Microcontroller
- IR Transmitter LED (Pin 13)
- Tactile push buttons (see `main.py` for exact GPIO pin mapping)

## Credits & Libraries
The non-blocking IR transmission and NEC/Samsung protocol encoding (`ir_tx.py` and `nec.py`) were written by [Peter Hinch](https://github.com/peterhinch/micropython_ir) and are used under the MIT License. 

The hardware pin mapping, debouncing logic, and main execution loop (`main.py`, `boot.py`) are custom-built for this specific controller layout.

## License
MIT License
