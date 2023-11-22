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
medium_motor = Motor(Port.C)

## sensors
ultra_sensor = UltrasonicSensor(Port.S4)
color_sensor = ColorSensor(Port.S3)
gyro_sensor = GyroSensor(Port.S2)

## robot
WHEEL_DIAMETER = 42
AXLE_TRACK = 151

robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)

## variables
### Calculate the light threshold. Choose values based on your measurements.
BLACK = 6
WHITE = 65
THRESHOLD = (BLACK + WHITE) / 2
PROPORTIONAL_GAIN = 0.3


LINE_SPEED = 200
STRAIGHT_SPEED = 140
GRAB_DOWN_SPEED = 500
GRAB_UP_SPEED = -1000

START_LENGTH = 142
ARM_LENGTH = 262
WHEEL_ARM = 186.5

def reflection():
    i = 0
    print("Measuring. Press to proceed.")
    while True:
        i += 1
        if i % 10 == 0:
            value = color_sensor.reflection()
            print(value)
            ev3.screen.print(value)
        if Button.CENTER in ev3.buttons.pressed():
            print("Measure ended")
            break

def celebration():
    ev3.light.on(Color.RED)
    wait(70)
    ev3.light.on(Color.BLUE)
    wait(70)
    ev3.light.on(Color.YELLOW)
    wait(70)
    ev3.light.on(Color.GREEN)
    wait(70)
    ev3.speaker.beep(440, 6000)

def ultra(distance, speed=LINE_SPEED):
    if ultra_sensor.distance() > distance:
        while ultra_sensor.distance() > distance:
            deviation = THRESHOLD - color_sensor.reflection()
            turn_rate = PROPORTIONAL_GAIN * deviation
            robot.drive(speed, turn_rate)
    else:
        while ultra_sensor.distance() < distance:
            deviation = THRESHOLD - color_sensor.reflection()
            turn_rate = PROPORTIONAL_GAIN * deviation
            robot.drive(- speed, - turn_rate)

def circle_to(angle, speed=STRAIGHT_SPEED):
    omega = speed / ARM_LENGTH * 360 / 2 / 3.1415
    if angle > 0:
        angle -= 1
        while robot.angle() < angle:
            robot.drive(speed, omega)
    else:
        angle += 1
        while robot.angle() >= angle:
            robot.drive(speed, -omega)
    robot.stop()
    left_motor.brake()
    right_motor.brake()

def circle(angle, speed=STRAIGHT_SPEED):
    first_angle = robot.angle()
    omega = speed / ARM_LENGTH * 360 / 2 / 3.1415
    if angle > 0:
        angle -= 1
        while robot.angle() - first_angle < angle:
            robot.drive(-speed, omega)
    else:
        angle += 1
        while robot.angle() - first_angle >= angle:
            robot.drive(speed, -omega)
    robot.stop()
    left_motor.brake()
    right_motor.brake()


def turn_to(end_angle):
    current_angle = robot.angle()
    turn_angle = end_angle - current_angle
    robot.turn(turn_angle)

def press_to_start():
    ev3.screen.print("Press to start")
    while True:
        if Button.CENTER in ev3.buttons.pressed():
            ev3.screen.print("Starting")
            break

def line_qube(proportional_gain=PROPORTIONAL_GAIN, speed=LINE_SPEED):
    track = robot.distance()
    while ultra_sensor.distance() > 40:
        deviation = THRESHOLD - color_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(speed, turn_rate)
        if robot.distance() > track + 500:
            robot.stop()
            celebration()
            exit()
    robot.stop()

def line():
    first_distance = robot.distance()
    if robot.distance() < distance:
        while robot.distance() - first_distance < distance:
            deviation = THRESHOLD - color_sensor.reflection()
            turn_rate = PROPORTIONAL_GAIN * deviation
            robot.drive(speed, turn_rate)
    else:
        while robot.distance() - first_distance > distance:
            deviation = THRESHOLD - color_sensor.reflection()
            turn_rate = PROPORTIONAL_GAIN * deviation
            robot.drive(- speed, - turn_rate)
    robot.stop()
    left_motor.brake()
    right_motor.brake()

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

def straight(distance, speed=STRAIGHT_SPEED):
    first_distance = robot.distance()
    if robot.distance() - first_distance < distance:
        while robot.distance() - first_distance < distance:
            robot.drive(speed, 0)
        robot.stop()
    else:
        while robot.distance() - first_distance > distance:
            robot.drive(- speed, 0)
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
    medium_motor.run_angle(10000, -480)
    medium_motor.run_until_stalled(GRAB_UP_SPEED, then=Stop.HOLD)

def grab():
    medium_motor.run_until_stalled(GRAB_DOWN_SPEED, then=Stop.HOLD)
    medium_motor.run_until_stalled(GRAB_UP_SPEED, then=Stop.HOLD)

#final_circle_iltra
def main():
    robot.reset()
    let_go()
    reflection()
    press_to_start()
    straight_to(START_LENGTH)
    first_grab()
    for i in range(3):
        line_qube()
        grab()
    line_to(1292)
    one = 1292

    circle(-90)
    robot.reset()

    for i in range(3):
        line_qube()
        grab()
    line_to(925)

    circle(-180)

    robot.reset()
    ev3.screen.print(robot.distance())
    straight_to(280, 300)
    ev3.screen.print(robot.distance())
    let_go()
    wait(800)
    straight(0, 300)
    ev3.screen.print(robot.distance())

    circle(90)

    robot.reset()
    let_go()
    for i in range(4):
        line_qube()
        grab()
    
    line_to(1443)
    circle(-90)

    for i in range(3):
        line_qube()
        grab()

    circle(-180)

    robot.reset()
    straight_to(280, 10000)
    let_go()
    wait(800)
    straight_to(0, 1000)

    celebration()


if __name__ == "__main__":
    ev3.speaker.beep()

    main()

    ev3.speaker.beep()
