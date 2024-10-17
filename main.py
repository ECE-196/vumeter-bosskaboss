import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,

    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
max = 0
cycle = 0
while True:
    volume = microphone.value

    print(volume)

    for i in range(0,11):
        leds[i].value = 0
    for i in range(max):
        leds[i].value = 1
        
    #Extra credit
    if max < volume//4367:
        max = volume//4367
    cycle = cycle + 1
    if cycle > 30:
        cycle = 0
        max = max - 1

    sleep(.01)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
