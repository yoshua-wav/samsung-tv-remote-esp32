from machine import Pin
from nec import NEC
import time

# Init IR sender (Samsung protocol)
ir_sender = NEC(Pin(13))
ir_sender.samsung = True
TV_ADDR = 0x07

# Button mapping: (GPIO, Name, Hex)
button_config = [
    (14, "Power", 0x02),  # D14
    (27, "Back", 0x58),  # D27
    (26, "Home", 0x79),  # D26
    (25, "OK", 0x68),  # D25
    (33, "Up", 0x60),  # D33
    (32, "Down", 0x61),  # D32
    (23, "Left", 0x65),  # D23
    (22, "Right", 0x62),  # D22
    (21, "Volume-Up", 0x07),  # D21
    (19, "Volume-Down", 0x0B),  # D19
    (18, "Start/Stop", 0x4F),  # D18
    (17, "Rewind", 0x49),  # D17
    (16, "Skip", 0x52)  # D16
]

# Initialize GPIO pins
buttons = []
for pin_num, name, ir_code in button_config:
    pin_obj = Pin(pin_num, Pin.IN, Pin.PULL_UP)
    buttons.append((pin_obj, name, ir_code))

print("System ready. Waiting for input...")

# Main loop
while True:
    for pin_obj, name, ir_code in buttons:
        if pin_obj.value() == 0:
            print(f"[{name}] pressed -> Sending: {hex(ir_code)}")
            ir_sender.transmit(TV_ADDR, ir_code, 0)
            time.sleep(0.3)  # Simple debounce

    time.sleep(0.01)  # Prevent CPU hogging