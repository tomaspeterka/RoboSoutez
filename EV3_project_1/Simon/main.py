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
ultra_sensor = UltrasonicSensor(Port.S4)
line_sensor = ColorSensor(Port.S3)
# touch_sensor = TouchSensor(Port.S2)

## base
base = DriveBase(left_motor, right_motor, wheel_diameter=42, axle_track=151)

## variables
### Calculate the light threshold. Choose values based on your measurements.
BLACK = 6
WHITE = 65
THRESHOLD = (BLACK + WHITE) / 2
PROPORTIONAL_GAIN = 0.7

BASIC_SPEED = 300
STROKE = 530
GRAB_DOWN_SPEED = 300
GRAB_UP_SPEED = 1000

def measure_distance():
    while True:
        print(length_sensor.distance())

def measure_stroke():
    medium_motor.reset_angle(0)
    while True:
        print(medium_motor.angle())

def line_move(speed=BASIC_SPEED, proportional_gain=PROPORTIONAL_GAIN):
    deviation = THRESHOLD - line_sensor.reflection()
    turn_rate = PROPORTIONAL_GAIN * deviation
    #print(line_sensor.reflection(), " ", deviation, " ", turn_rate)
    base.drive(speed, turn_rate)

def begin_down(boolean=False):
    if boolean == True:
        medium_motor.run_angle(GRAB_DOWN_SPEED, STROKE)
        print("finish")

def press_to_start():
    print("Press to start")
    while True:
        pressed = touch_sensor.pressed()
        if pressed == True:
            print("Starting programme")
            break

def first_grab():
    medium_motor.reset_angle(STROKE)
    medium_motor.run_angle(GRAB_UP_SPEED, - STROKE)
    print(medium_motor.angle())

def grab():
    medium_motor.reset_angle(0)
    medium_motor.run_angle(GRAB_DOWN_SPEED, STROKE)

    print(medium_motor.angle())

    medium_motor.reset_angle(STROKE)
    medium_motor.run_angle(GRAB_UP_SPEED, - STROKE)

    print(medium_motor.angle())

def big_four():
    first_grab()
    for i in range(3):
        while ev3.distance() < 280:
            line_move()
        grab()

# Write your program here.
def main():
    ev3.speaker.beep()
    base.reset()
    begin_down(False)   #True if wanted
    while ultra_sensor.distance() > 40:
        line_move()   ß ß ß
    first_grab()
    for i in range(2):
        while ev3.distance() < 280:
            line_move()
        grab()
    ev3.speaker.beep()

if __name__ == "__main__":
    # main()
    while True:
        line_move()
