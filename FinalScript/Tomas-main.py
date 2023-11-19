#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep

# This program requires LEGO EV3 MicroPython v2.0 or higher.

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
medium_motor = Motor(Port.C)

line_sensor = ColorSensor(Port.S3)
obstacle_sensor = UltrasonicSensor(Port.S4)


robot = DriveBase(left_motor, right_motor, wheel_diameter=42, axle_track=151)


# Write your program here.
BLACK = 6
WHITE = 65
THRESHOLD = (BLACK + WHITE) / 2
DRIVE_SPEED = 1000
BASIC_SPEED = 1000
PROPORTIONAL_GAIN = 0.7
DISTANCE_BETWEEN_CUBES = 280
STROKE = 525
GRAB_DOWN_SPEED = 300
GRAB_UP_SPEED = 1000

def first_grab():
    medium_motor.reset_angle(STROKE)
    medium_motor.run_angle(GRAB_UP_SPEED, - STROKE)
    print("Grabbed first cube")

def grab(cube_number):
    medium_motor.reset_angle(0)
    medium_motor.run_angle(GRAB_DOWN_SPEED, STROKE)

    medium_motor.reset_angle(STROKE)
    medium_motor.run_angle(GRAB_UP_SPEED, - STROKE)
    print("Grabbed ", cube_number, " cube")

def fill_out():
    print("Filling out !!!")
    medium_motor.reset_angle(0)
    medium_motor.run_angle(200, 535)
    robot.straight(-100)

def line_move(speed=BASIC_SPEED, proportional_gain=PROPORTIONAL_GAIN):
    deviation = THRESHOLD - line_sensor.reflection()
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(BASIC_SPEED, turn_rate)




robot.straight(DISTANCE_BETWEEN_CUBES/2 + 50)
first_grab()

for i in range(2):
    while obstacle_sensor.distance() > 40:
        line_move()
    robot.stop()
    grab(i)

wait(300)
while obstacle_sensor.distance() > 280:
    print(obstacle_sensor.distance())
    line_move()
    wait(100)
robot.stop()

robot.turn(-90)



