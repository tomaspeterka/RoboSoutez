#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys
import threading

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Initialization
ev3 = EV3Brick()

# motors
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
medium_motor = Motor(Port.C)

# sensors
#ultra_sensor = UltrasonicSensor(Port.S___)
color_sensor = ColorSensor(Port.S4)
#gyro_sensor = GyroSensor(Port.S___)


GAMING_TIME = 90000
POSSIBLE_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.BLACK, Color.BROWN, Color.ORANGE, Color.WHITE, Color.PURPLE]
robot = DriveBase(left_motor, right_motor, 42, 150)

# My functions
def grab_down():
    medium_motor.run_until_stalled(1000, then=Stop.COAST , duty_limit=70)
    print("Grabbed down")

def grab_up():
    medium_motor.run_angle(1000, -510, then=Stop.HOLD, wait=True)
    print("Grabbed up")

def free_cube():
    medium_motor.run_angle(1000, -50, then=Stop.BRAKE, wait=True)
    print("Freedom for cube")

def open_door():
    medium_motor.run_until_stalled(-1000, then=Stop.COAST , duty_limit=70)

def stop_all_motors():
    left_motor.brake()
    right_motor.brake()
    medium_motor.brake()

def grab_cube():
    while True:
        if color_sensor.color() in POSSIBLE_COLORS:
            wait(700)
            free_cube()
            grab_down()
            grab_up()
            
        

# MAIN
def final_beep():
    wait(GAMING_TIME - 7000)
    ev3.screen.clear()
    stop_all_motors()
    ev3.screen.print("      The end")
    ev3.speaker.beep(300, 5000)
    sys.exit()

def main():
    ev3.screen.print()       
    ev3.screen.print("      RUNNING...")
    ##left_motor.run_time(100, GAMING_TIME, then=Stop.HOLD, wait=False)
    #right_motor.run_time(100, GAMING_TIME, then=Stop.HOLD, wait=False)

    grab_cube()
    

t1 = threading.Thread(target=final_beep)
t2 = threading.Thread(target=main)


# CALIBRATION
#while True:
    #print(medium_motor.angle())
grab_down()
grab_up()

ev3.screen.print("  I'm ready now!")
ev3.screen.print("   Press to start")
ev3.speaker.beep(300, 1000)

robot.settings(1000, 300, 1000, 300)
robot.straight(3000)

while True:
    if Button.CENTER in ev3.buttons.pressed(): 
        ev3.speaker.beep()
        t1.start()
        t2.start()
        wait(GAMING_TIME - 1000)
