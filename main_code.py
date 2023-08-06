import time
import board
import digitalio
import adafruit_adxl34x
import adafruit_dotstar as dotstar
import neopixel

"""
Friendship Bracelet v1.0
    This is the first version of the code for the Friendship Bracelet. It is only for the cool kids.

Initial Features:
    Best Friend Clasp:
        - Hold Friend's forearm for 10 seconds while singing friendship song
        - At the end, both bracelets will light up and buzz for the next 5 minutes
    Power Fist Charge Up:
        - This is for when you really need to draw out your super powers!!!
        - Make a fist and shake for 7 seconds
        - At the end of 7 seconds, the bracelet will buzz and light up for the next 30 seconds
    Motion Detection based Sleep Mode for Power Saving

Upcoming? Feature List:
    Secret Handshake
    Avengers Assemble
    Sync with Smart Backpack

Hardware Needed (per bracelet):
    Adafruit Gemma M0
    ADXL343 accelerometer
    Hall Effect Sensor
    Adafruit LED Sequins (atleast 5)
    I2S Mems Microphone
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
# For ADXL343
i2c = board.I2C()  # uses board.SCL and board.SDA
accelerometer = adafruit_adxl34x.ADXL343(i2c)
accelerometer.enable_motion_detection(threshold=10)
accelerometer.enable_tap_detection(tap_count=2,threshold=20, duration=50)
accelerometer.enable_freefall_detection(threshold=10,time=25)

# for the onboard red LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# for the hall effect sensor
switch = digitalio.DigitalInOut(board.D2)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# for the buzzer
buzzer = digitalio.DigitalInOut(board.D0)
buzzer.direction = digitalio.Direction.OUTPUT
buzzer.pull = digitalio.Pull.DOWN

# for the sequins
sequins = digitalio.DigitalInOut(board.D1)
sequins.direction = digitalio.Direction.OUTPUT
sequins.pull = digitalio.Pull.UP


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

# Startup Sequence ####################################################
# Runs once after toggling the power switch
# Buzz the buzzer twice
for i in range(2):
    buzzer.value = True
    time.sleep(0.1)
    buzzer.value = False
    time.sleep(0.1)

# Turn on the Sequins
sequins.value = True

# Cycle the dotstar rainbow
for i in range(255):
    dot[0] = wheel(i)
    dot.show()

# Flash Each Neopixel Red
# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)
# for pixel in range(4):
#     pixels[pixel] = (255, 0, 0)
#     time.sleep(0.1)
#     pixels[pixel] = (0, 0, 0)
#     time.sleep(0.1)

# Turn off the Sequins
sequins.value = False

# Main Loop ##########################################################
while True:
    print("Hello World!")

    # Print the accelerometer values
    # print("%f %f %f" % accelerometer.acceleration)
    # print("Dropped: %s" % accelerometer.events["freefall"])
    # print("Tapped: %s" % accelerometer.events["tap"])
    # print("Motion detected: %s" % accelerometer.events["motion"])

    # Placing a Magnet near the Hall Effect Sensor will turn the LED on
    if switch.value:
        led.value = False
    else:
        led.value = True
    time.sleep(0.01)  # debounce delay

    time.sleep(0.5) # adjust this to change the speed of the loop
