#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import measure

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Initialization
ev3 = EV3Brick()

## motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
medium_motor = Motor(Port.C)

## sensors
ultra_sensor = UltrasonicSensor(Port.S4)
color_sensor = ColorSensor(Port.S3)
gyro_sensor = GyroSensor(Port.S2)

## robot
robot = DriveBase(left_motor, right_motor, wheel_diameter=42, axle_track=151)

## variables
### Calculate the light threshold. Choose values based on your measurements.
BLACK = 6
WHITE = 65
THRESHOLD = (BLACK + WHITE) / 2
PROPORTIONAL_GAIN = 0.25

LINE_SPEED = 200
STRAIGHT_SPEED = 140
GRAB_DOWN_SPEED = 500
GRAB_UP_SPEED = -1000

ARM_LENGTH = 265

def turn_to(end_angle):
    current_angle = robot.angle()
    turn_angle = end_angle - current_angle
    robot.turn(turn_angle)

def press_to_start():
    print("Press to start")
    while True:
        if Button.CENTER in ev3.buttons.pressed():
            print("Starting")
            break

def line_qube(proportional_gain=PROPORTIONAL_GAIN, speed=LINE_SPEED):
    while ultra_sensor.distance() > 40:
        deviation = THRESHOLD - color_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(speed, turn_rate)
    robot.stop()

def line_to(distance, speed=LINE_SPEED):
    if robot.distance() < distance:
        while robot.distance() < distance:
            deviation = THRESHOLD - color_sensor.reflection()
            turn_rate = PROPORTIONAL_GAIN * deviation
            robot.drive(speed, turn_rate)
        robot.stop()
    else:
        while robot.distance() > distance:
            deviation = THRESHOLD - color_sensor.reflection()
            turn_rate = PROPORTIONAL_GAIN * deviation
            robot.drive(- speed, - turn_rate)
        robot.stop()

def straight_to(distance, speed=STRAIGHT_SPEED):
    if robot.distance() < distance:
        while robot.distance() < distance:
            robot.drive(speed, 0)
        robot.stop()
    else:
        while robot.distance() > distance:
            robot.drive(- speed, 0)
        robot.stop()

def let_go():
    medium_motor.run_until_stalled(GRAB_DOWN_SPEED, then=Stop.HOLD)

def first_grab():
    medium_motor.run_until_stalled(GRAB_UP_SPEED, then=Stop.HOLD)

def grab():
    medium_motor.run_until_stalled(GRAB_DOWN_SPEED, then=Stop.HOLD)
    medium_motor.run_until_stalled(GRAB_UP_SPEED, then=Stop.HOLD)

# Write your program here.
def main():
    robot.reset()
    let_go()
    measure.reflection()
    line_to(156)
    first_grab()
    for i in range(2):
        line_qube()
        grab()
    line_to(156 + 280*3 - 33)
    straight_to(156 + 280*4 - 11)
    one = 156 + 280*4 - 11
    print("Is", 156 + 280*4 - 11, robot.distance(), "?")

    print(robot.angle())
    press_to_start()
    turn_to(-90)
    print(robot.angle())
    press_to_start()

    straight_to(one + 280 + 22)
    for i in range(3):
        line_qube()
        grab()
    line_to(one + 280*4)
    straight_to(one + 280*5 + 22)
    two = one + 280*5 + 22
    grab()

    print(robot.angle())
    press_to_start()
    turn_to(-180)
    print(robot.angle())
    press_to_start()


    straight_to(two + 280 + 22)
    line_to(two + 280*2 + 22)
    three = two + 280*2 + 22
    let_go()

    print(robot.angle())
    press_to_start()
    turn_to(-270)
    print(robot.angle())
    press_to_start()


    straight_to(three + 280 + 22)
    line_to(three + 280*2 + 22)
    line_to(three + 280 + 22)
    straight_to(three)

    print(robot.angle())
    press_to_start()
    turn_to(-180)
    print(robot.angle())
    press_to_start()





if __name__ == "__main__":
    ev3.speaker.beep()

    main()

    ev3.speaker.beep()
