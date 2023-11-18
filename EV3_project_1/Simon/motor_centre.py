#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Initialization
ev3 = EV3Brick()

## motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
medium_motor = Motor(Port.D)

## sensors
line_sensor = ColorSensor(Port.S3)
length_sensor = UltrasonicSensor(Port.S2)

## base
base = DriveBase(left_motor, right_motor, wheel_diameter=42, axle_track=151)

# Write your program here.
def main():
    ev3.speaker.beep()
    base.reset()
    base.straight(1000, 0)
    #base.drive(0, 360)
    ev3.screen.print(distance())
    

if __name__ == "__main__":
    main()