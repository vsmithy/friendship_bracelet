import time
import board
import digitalio
import adafruit_dotstar as dotstar
from rainbowio import colorwheel
import neopixel

"""
Friendship Bracelet v0.5
    This is the first version of the code for the Friendship Bracelet. It is only for the cool kids.

** I needed to order a new accelerometer and GPIO expander, so those are not included in this code yet. **

Initial Features:
    Best Friend Clasp:
        - Hold Friend's forearm for 10 seconds while singing friendship song
        - At the end, both bracelets will light up and buzz for the next 5 minutes
    Power Fist Charge Up (once additional hardware is added):
        - This is for when you really need to draw out your super powers!!!
        - Make a fist and shake for 7 seconds
        - At the end of 7 seconds, the bracelet will buzz and light up for the next 30 seconds
    Motion Detection based Sleep Mode for Power Saving

Upcoming? Feature List:
    Secret Handshake
    Avengers Assemble
    Sync with Smart Backpack
    Error states and logging
    
Hardware Needed (per bracelet):
    Adafruit Gemma M0
    ADXL343 accelerometer
    Hall Effect Sensor
    Adafruit LED Sequins (atleast 5)
    GPIO Expander
    2032 coin cell battery holder
    2x 2032 coin cell batteries
    Small Magnet
    Conductive Thread
    Regular Thread
    Clear Nail Polish
    On/Off Switch
    Neopixels (4)
    Fabric or Leather to make the Bracelet
    Clasp or buttons to close the bracelet on your wrist

Tutorial, Circuit Diagram, and Additional Information: https://vsmith.me

"""

# Setup ###############################################################
# for the onboard red LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# for the hall effect sensor
switch = digitalio.DigitalInOut(board.D1)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# for the buzzer
buzzer = digitalio.DigitalInOut(board.D2)
buzzer.direction = digitalio.Direction.OUTPUT
buzzer.pull = digitalio.Pull.DOWN

# for the neopixels
pixel_pin = board.A2
num_pixels = 4
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)


# Helper Functions ####################################################
# Helper to debounce a pin
def debounce(pin):
    last = pin.value
    while True:
        current = pin.value
        if current != last:
            time.sleep(0.01)
            current = pin.value
        last = current
        yield current

# # Helper to give us a nice dotstar color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

# Helper to give us a nice neopixel color swirl
def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

# Helper to give us a nice neopixel color swirl
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


# Startup Sequence ####################################################
# Runs once after toggling the power switch
# Blink the onboard LED
for i in range(3):
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)

# Turn on all Neopixels
pixels.fill(RED)
pixels.show()
time.sleep(1)
pixels.fill(GREEN)
pixels.show()
time.sleep(1)
pixels.fill(BLUE)
pixels.show()
time.sleep(1)

# Buzz the buzzer twice
for i in range(2):
    buzzer.value = True
    time.sleep(0.1)
    buzzer.value = False
    time.sleep(0.1)

# Cycle the dotstar rainbow
for i in range(255):
    dot[0] = wheel(i)
    dot.show()

# Rainbow Chase the neopixels
color_chase(RED, 0.1)  # Increase the number to slow down the color chase
color_chase(YELLOW, 0.1)
color_chase(GREEN, 0.1)
color_chase(CYAN, 0.1)
color_chase(BLUE, 0.1)
color_chase(PURPLE, 0.1)
rainbow_cycle(0)  # Increase the number to slow down the rainbow
pixels.deinit()  # Finished with the Neopixels for now


# Main Loop ##########################################################
while True:
    print("Hello World!")

    # Placing a Magnet near the Hall Effect Sensor will turn the LED on
    if switch.value:
        led.value = False
    else:
        led.value = True
    time.sleep(0.01)  # debounce delay

    time.sleep(0.5) # adjust this to change the speed of the loop
