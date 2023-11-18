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

length_sensor = UltrasonicSensor(Port.S2)

## base

# Write your program here.
def main():
    ev3.speaker.beep()
    while True:
        ev3.screen.print(length_sensor.distance())
    

if __name__ == "__main__":
    main()
