#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.display import Display

import time
import math
import threading
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


ev3 = EV3Brick()
ultrasonic = UltrasonicSensor(Port.S1)
gyro = GyroSensor(Port.S3)
button = TouchSensor(Port.S2)
color = ColorSensor(Port.S4)


left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
motor_d = Motor(Port.A)
base = DriveBase(left_motor, right_motor, 43.2, 20)

base.settings(1000, 800, 100, 1)

max_motor_speed = 600  # Replace with your specific maximum motor speed
black = 13
line_following_enabled = True

# Function to convert percentage speed to actual speed based on max speed



def calculate_speed(percentage_speed):
    return (percentage_speed / 100) * max_motor_speed


def unstuck():
    base.drive(calculate_speed(20),0)
    motor_d.run(-calculate_speed(70))
    speed = 15
    while not button.pressed():
        pass
    motor_d.run(-calculate_speed(10))
    base.stop()
    while button.pressed():
        wait(1)
    motor_d.stop()
    motor_d.run_angle(-calculate_speed(7),360*0.5, then=Stop.HOLD)
    base.settings(1000, 100, 100, 1)

    base.straight(-80)
    base.stop()
    base.settings(1000, 800, 100, 1)

# Function to perform the described sequence
def stuck(enable_motors=True):
    if enable_motors:
        left_motor.run(calculate_speed(40))
        right_motor.run(calculate_speed(40))
        time.sleep(0.4)
        left_motor.stop()
        right_motor.stop()
    else:
        base.straight(15)
        speed = 7
        # time.sleep(0.5)
        base.drive(calculate_speed(speed), 0)
        motor_d.run(-calculate_speed(70))
        speed = 15
        
        counter1 = 0
        counter2 = 0
        while not button.pressed():
            error1 = 55 - counter1
            error2 = 45 - counter2
            if color.reflection() < black:
                counter1+=0.05
                counter2 =0
                if error1 < 0:
                    error1 = 0
                base.drive(calculate_speed(speed), error1)
            else:
                counter2+=0.05
                counter1 =0
                if error2 < 0:
                    error2 = 0
                base.drive(calculate_speed(speed), -error2)
        base.stop()
        motor_d.run(-calculate_speed(20))

        while button.pressed():
            wait(1)
        motor_d.stop()
        motor_d.run_angle(-calculate_speed(30),360*0.13, then=Stop.HOLD)
    
    
        # time.sleep(0.6)
    
    

    motor_d.run(calculate_speed(170))
    while not button.pressed():
        wait(1)
    
    
    motor_d.stop()
    motor_d.reset_angle(0)
    br_time = time.time() + 1
    motor_d.run(calculate_speed(170))
    while True:
        if motor_d.angle() >= 730 or time.time() > br_time:
            print("Co je pravda:" + str(motor_d.angle() >= 725) + " nebo " + str(time.time() > br_time))
            motor_d.stop()
            motor_d.hold()
            break
            
            
    
    

    if ultrasonic.distance() < 70:
        base.straight(35)
        motor_d.run(-calculate_speed(70))
        while not button.pressed():
            wait(1)
        motor_d.run(-calculate_speed(20))

        while button.pressed():
            wait(1)
        motor_d.stop()
        motor_d.run_angle(-calculate_speed(30),360*0.13, then=Stop.HOLD)
        time.sleep(0.6)
        motor_d.run(calculate_speed(170))
        while not button.pressed():
            wait(1)
        print("odzmáčklo")
        while button.pressed():
            wait(1)
        motor_d.stop()
        motor_d.reset_angle(0)
        br_time = time.time() + 1
        motor_d.run(calculate_speed(170))
        while True:
            if motor_d.angle() >= 725 or time.time() > br_time:
                break
                motor.stop()
                motor_d.hold() 
    
    

    


def g_reset():
    gyro.speed()
    gyro.angle()
    time.sleep(0.5)


def g_turn(target_angle_deg, max_speed=30):
    while True:
        # Read the current gyro angle
        current_angle = gyro.angle()

        # Calculate the error (the difference between target and current angles)
        error = target_angle_deg - current_angle

        # Define a proportional control constant (you can adjust this as needed)
        kp = 7

        # Calculate the motor speeds
        speed_adjustment = kp * error 

        # Set the motor speeds to turn in place
        

        # If the robot is very close to the target angle, break the loop
        if abs(error) < 1:
            break

        wait(10)
        print(current_angle)

    # Stop the motors when the desired angle is reached
    left_motor.stop()
    right_motor.stop()
    


# Function to maintain a constant distance from the wall


def line(speed, distance):
    
    
    if distance ==0:
        counter1 = -1
        counter2 = -1
        while True:
            error1 = 55 * (speed/30) - counter1
            error2 = 45 * (speed/30) - counter2
            if color.reflection() < black:
                counter1+=0.3
                counter2 =0
                if error1 < 0:
                    error1 = 0
                base.drive(calculate_speed(speed), error1)
            else:
                counter2+=0.02
                counter1 =0
                if error2 < 0:
                    error2 = 0
                base.drive(calculate_speed(speed), -error2)
            # Display data on the screen
            
            if ultrasonic.distance() < 72:
                base.stop()
                break
    
    else:

        counter1 = -3
        counter2 = -3
        base.reset()
        while True:
            error1 = 55 * (speed/30) - counter1
            error2 = 45 * (speed/30) - counter2
            if color.reflection() < black:
                counter1+=0.2
                counter2 =0
                if error1 < 0:
                    error1 = 0
                base.drive(calculate_speed(speed), error1)
            else:
                counter2+=0.05
                counter1 =0
                if error2 < 0:
                    error2 = 0
                base.drive(calculate_speed(speed), -error2)
            # Display data on the screen
            
            if left_motor.angle()/360*43.2 >= 190:
                print(str(left_motor.angle()/360*43.2))
                base.stop()
                break
def turn():
    base2 = DriveBase(left_motor, right_motor, 43.2, 155)
    print('uhel: ' + str(base2.angle()))

    base2.drive(220, -45)
    
    angl1 = base2.angle()
    while True:
        if base2.angle() <= -98:
            base2.stop()
            break
    base2.stop()
    print('uhel: ' + str(base2.angle()))
    base2.drive(calculate_speed(90), 0)

    while True:
        if color.reflection() < black or ultrasonic.distance() < 72:
            base2.stop()
            break
            time.sleep(0.5)
    

    
    time.sleep(2)
    base = DriveBase(left_motor, right_motor, 43.2, 30)
    base2 = DriveBase(left_motor, right_motor, 43.2, 30)      

def line2(speed, distance):
    
    
    if distance ==0:
        counter1 = -1
        counter2 = -1
        while True:
            error1 = 55 * (speed/30) - counter1
            error2 = 55 * (speed/30) - counter2
            if color.reflection() < black:
                counter1+=0.3
                counter2 =0
                if error1 < 0:
                    error1 = 0
                base.drive(calculate_speed(speed), error1)
            else:
                counter2+=0.02
                counter1 =0
                if error2 < 0:
                    error2 = 0
                base.drive(calculate_speed(speed), -error2)
            # Display data on the screen
            
            if ultrasonic.distance() < 72:
                base.stop()
                break




print("Start: " + str(time.time()))
start_time = time.time()
stuck(True)
line(70,0)
print("1." + str(time.time()))
stuck(False)
line(70,0)
print("2." + str(time.time()))
stuck(False)
print("3." + str(time.time()))
left_motor.reset_angle(0)
line(70,0)
print('vydalenost3: ' + str(left_motor.angle()/360*43.2))


stuck(False)
print('vydalenost3: ' + str(left_motor.angle()/360*43.2))
line(60,1)

turn()
# # line2(70,0)
# # stuck(False)
# # line2(60,0)
# # stuck(False)
# # line(260,0)
# # stuck(False)

# print("Konec: " + str(time.time()))
# print("Trvání: " + str(time.time()-start_time))
# stuck(False)
# stuck(False)


