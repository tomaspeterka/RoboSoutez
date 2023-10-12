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
ev3.screen.print("testing4 - Rozeznávání barev")
wait(5000)

# Write your program here.
ev3.speaker.beep()

while True:
    ev3.screen.print(color_sensor.rgb())
    # ev3.screen.print(color_sensor.reflection())
    # ev3.screen.print(color_sensor.ambient())
    # ev3.screen.print(color_sensor.color())
    wait(1000)


"""
POSSIBLE_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]

while True:
    color = color_sensor.color()
    if color in POSSIBLE_COLORS:
        print(f"It's a ", color)
    else:
        print("It's not red, green, blue neither yellow.")
"""