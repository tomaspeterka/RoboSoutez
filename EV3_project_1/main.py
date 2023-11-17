#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Initialization
ev3 = EV3Brick()

## motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
medium_motor = Motor(Port.C)

## sensors
length_sensor = UltrasonicSensor(Port.S3)
line_sensor = ColorSensor(Port.S2)
touch_sensor = TouchSensor(Port.S4)

## base
base = DriveBase(left_motor, right_motor, wheel_diameter=42, axle_track=151)

## variables
### Calculate the light threshold. Choose values based on your measurements.
BLACK = 6
WHITE = 65
threshold = (BLACK + WHITE) / 2
PROPORTIONAL_GAIN = 0.7

def measure_stroke():
    medium_motor.reset_angle(0)
    while True:
        print(medium_motor.angle())

def line_move():
    while True:
        deviation = threshold - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        #print(line_sensor.reflection(), " ", deviation, " ", turn_rate)
        base.drive(100, turn_rate)

def begin_down(boolean=False):
    if boolean == True:
        medium_motor.run_angle(800, 530)
        print("finish")

def press_to_start():
    print("Press to start")
    while True:
        pressed = touch_sensor.pressed()
        if pressed == True:
            print("Starting programme")
            break

def first_grab():
    medium_motor.reset_angle(530)
    medium_motor.run_angle(1000, -530)
    print(medium_motor.angle())

def grab():
    medium_motor.reset_angle(0)
    medium_motor.run_angle(200, 530)

    print(medium_motor.angle())

    medium_motor.reset_angle(530)
    medium_motor.run_angle(1000, -530)

    print(medium_motor.angle())


# Write your program here.
def main():
    ev3.speaker.beep()
    base.reset()
    begin_down(True) #True if wanted
    press_to_start()
    first_grab()
    wait(2000)
    for i in range(7):
        grab()
        wait(2000)
    #line_move()
    #ev3.screen.print(distance())
    ev3.speaker.beep()

if __name__ == "__main__":
    main()
    #measure_stroke()