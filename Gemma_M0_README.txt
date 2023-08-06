Welcome to CircuitPython!
#############################

Visit the Gemma M0 product page here for more info: 
                              https://adafruit.com/product/3501

To get started with CircuitPython, which comes built into your Gemm, visit:
    https://learn.adafruit.com/welcome-to-circuitpython

#############################

The Gemma has a very tiny disk drive so we have disabled Mac OS X indexing
which could take up that valuable space. 

So *please* do not remove the empty .fseventsd/no_log, .metadata_never_index 
or .Trashes files!

#############################

The pre-loaded demo shows off what your Gemma M0 can do with CircuitPython:
  * The built in DotStar LED can show any color, it will swirl through the rainbow
  * Pin A0 is a true analog output, you will see the voltage slowly rise
  * Pin A1 is an analog input, the REPL will display the voltage on this pin 
    (0-3.3V is the max range)
  * Pin A2 is a capacitive input, when touched, it will turn on the red LED. 
    If you update main.py to uncomment the relevant lines, it will act as a 
    mini keyboard and emulate an 'a' key-press whenever A2 is touched.

For more details on how to use CircuitPython, visit 
https://adafruit.com/product/3501
and check out all the tutorials we have!

#############################
CircuitPython Quick Start:

Changing the code is as easy as editing main.py in your favorite text editor. 

Our recommended editor is Mu, which is great for simple projects, and comes
with a built in REPL serial viewer! It is available for Mac, Windows & Linux
https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor

After the file is saved, CircuitPython will automatically reload the latest 
code. Try enabling the capacitive keyboard 
(HINT: look for the "# optional! uncomment below..." text)

Connecting to the serial port will give you access to sensor information, 
better error messages and an interactive CircuitPython (known as the REPL). 
On Windows we recommend Mu, Tera Term or PuTTY. 
On Mac OSX and Linux, use Mu or 'screen' can be used from a terminal.