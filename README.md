# Hack-a-Sketch

***TRIGGER WARNING:*** The code is just bad, it was a quick and dirty project and my first attempt at using an Arduino and using Python

## Overview
This project was created for Local Hack Day 2016, I chose this because I had never done a hackathon previously, wanted to learn some python, wanted put my Arduino to use, and because it's all I could think of creating with my very limited supply of electronic parts. The code is rather awful (but that's okay because it's in the spirit of hackathons!) but it worked so I shall call it a success!

### How it works
* The arduino reads the values from the board (potentiometers, accelerometer) and prints to 1 line on what the values are
* The python program reads in the line and splits up the values read from the arduino
* It will draw a line from the previous X and Y value read to the current one
  * Turning the 3rd potentiometer will change the colour of the point
  * Shaking the breadboard will trigger a "fade" to the pygame screen (blending mask which adds a value to each pixel's RGB values which in turn makes the screen appear to fade with each shake)
    * Shake is detected using a sliding window to register only 1 fade with 1 shake
    * Values for when a shake is detected was produced by plotting in OpenOffice me moving the breadboard in various ways and trying to see what a good threshold would be by guessing and checking

## Demo!
Click the image below to see a video of it in action!
[![](https://github.com/echubaty/Hack-a-Sketch/blob/master/images/20161204_015018_HDR.jpg)](https://www.youtube.com/watch?v=t8_YyP3FWt4&)


## Electronics
* 1 x Breadboard
* 1 x Arduino Mega 2560
* 1 x Accelerometer ADXL335
* 3 x Resistor
* 3 x Potentiometer (2 modded)
* 1 Fuckload x Jumper wires

#### Input pins
* A0 - X axis
* A1 - Y axis
* A2 - Z axis
* A8 - Left pot
* A9 - Right pot
* A10 - Colour pot

I had to modify the 2 potentiometers by removing the physical stop to allow it to turn 360 degrees. This was a hack on it's all on it's own. I originally planned to use 2 digital rotary encoders but unfortunately only had 1. I tried to handle the sporatic voltage reads when the sweeper head on the pot was between the resistance element in software and with a pull-down resistor but even this didn't work out the best at times.
<br>
A problem I faced when testing this mod was that I burned one of the pots I prepared for the competition. Luckily I had some solder and a lighter and walked outside of the competition to solder that bad boy up.

I carried out the mod by:

* open the pot by bending the tabs down and removing the bottom
* break the physical seperation off with some wire cutters
* use a ton of electric tape over the middle rail to not short it with the sweeper arm
* bend the tabs back to reassemble and solder some leads on too

![](https://github.com/echubaty/Hack-a-Sketch/blob/master/images/20161203_021022.jpg "")
![](https://github.com/echubaty/Hack-a-Sketch/blob/master/images/20161203_021156.jpg "")
![](https://github.com/echubaty/Hack-a-Sketch/blob/master/images/20161203_021234.jpg "")

![](https://github.com/echubaty/Hack-a-Sketch/blob/master/images/20161203_235645.jpg "")
![](https://github.com/echubaty/Hack-a-Sketch/blob/master/images/20161203_235655.jpg "")


## Dependencies
* Python 2.7
  * PySerial
  * Pygame
  
  
## Instructions
* Install dependencies
* Upload HackASketch/HackASketch.ino to the arduino with baud rate of 9600 using Arduino IDE
* Ensure that the arduino is connected to /dev/ttyACM0 or change in hacksketch_main.py
* Just run hacksketch_main.py and everything should magically work!


## Contact
Feel free to create an issue or submit a pull request if you so desperately wanted to use this piece of junk and improve it. You could even leave an issue to just roast me but I hope you still enjoyed the concept!
