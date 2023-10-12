#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3 = EV3Brick()
ev3.screen.print("testing1 - Základní funkce (pojezd, text, pípání)")
wait(5000)


# Write your program here.
ev3.screen.draw_text(40, 50, "thinking")
wait(5000)


ev3.speaker.beep()



left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=40, axle_track=104)

# Go forward and backwards for one meter.
robot.straight(1000)
ev3.speaker.beep()

robot.straight(-1000)
ev3.speaker.beep()

# Turn clockwise by 360 degrees and back again.
robot.turn(360)
ev3.speaker.beep()

robot.turn(-360)
ev3.speaker.beep()
