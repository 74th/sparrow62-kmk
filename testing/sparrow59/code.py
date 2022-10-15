import digitalio
import time
import board

target_pins = [
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP23,
    board.GP24,
    board.GP25,
    board.GP26,
    board.GP27,
    board.GP28,
    board.A3,
]
pins = []
for target in target_pins:
    pin = digitalio.DigitalInOut(target)
    pin.direction = digitalio.Direction.OUTPUT
    pins.append(pin)

while True:
    for i, pin in enumerate(pins):
        pin.value = i % 2 == 0
    print("switch1")
    time.sleep(3)
    for i, pin in enumerate(pins):
        pin.value = i % 2 == 1
    print("switch2")
    time.sleep(3)
