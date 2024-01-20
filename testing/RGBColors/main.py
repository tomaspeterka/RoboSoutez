#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Initialize the Color Sensor. It is used to detect the color of the objects.
color_sensor = ColorSensor(Port.S3)

# Create your objects here.
ev3 = EV3Brick()
ev3.screen.print("testing5 - RGB spektrum")
wait(5000)

# Write your program here.
ev3.speaker.beep()

def is_yellow(rgb):
    r, g, b = rgb
    yellow_red_threshold = 150
    yellow_green_threshold = 150
    yellow_blue_threshold = 50
    return r > yellow_red_threshold and g > yellow_green_threshold and b < yellow_blue_threshold

def is_green(rgb):
    r, g, b = rgb
    green_threshold = 100
    return g > green_threshold and r < green_threshold and b < green_threshold

def is_blue(rgb):
    r, g, b = rgb
    blue_threshold = 100
    return b > blue_threshold and r < blue_threshold and g < blue_threshold

def is_red(rgb):
    r, g, b = rgb
    red_threshold = 150
    green_threshold = 50
    return r > red_threshold and g < green_threshold and b < green_threshold

def is_black(rgb):
    r, g, b = rgb
    black_threshold = 50
    return r < black_threshold and g < black_threshold and b < black_threshold


while True:
    
    # get RGB from ev3 color sensor
    rgb_values = (color_sensor.rgb())

    if is_yellow(rgb_values):
        print("The color is YELLOW!")

    if is_green(rgb_values):
        print("The color is green!")

    if is_blue(rgb_values):
        print("The color is blue!")

    if is_red(rgb_values):
        print("The color is red!")

    if is_black(rgb_values):
        print("The color is black!")

    """
    # Use this with elif
    else:
        ev3.screen.print("The color is not KNOWN.")
        ev3.screen.print(" !!!!! ")
    """


