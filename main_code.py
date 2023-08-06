import time
import board
import digitalio
import adafruit_adxl34x

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

Upcoming Feature List:
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
    Fabric or Leather to make the Bracelet
    Clasp or buttons to close the bracelet on your wrist

Tutorial, Circuit Diagram, and Additional Information: https://mywebsite.com

"""

# Setup ###############################################################
# For ADXL343
# i2c = board.I2C()  # uses board.SCL and board.SDA
# accelerometer = adafruit_adxl34x.ADXL343(i2c)
# accelerometer.enable_motion_detection(threshold=10)
# accelerometer.enable_tap_detection(tap_count=2,threshold=20, duration=50)
# accelerometer.enable_freefall_detection(threshold=10,time=25)

# for the onboard red LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# for the hall effect sensor
switch = digitalio.DigitalInOut(board.D2)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP


# Helper Functions ####################################################
# Helper to debounce a pin
# def debounce(pin):
#     last = pin.value
#     while True:
#         current = pin.value
#         if current != last:
#             time.sleep(0.01)
#             current = pin.value
#         last = current
#         yield current


# Main Loop
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
