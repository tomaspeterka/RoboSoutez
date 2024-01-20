#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from time import sleep
from math import e


# This program requires LEGO EV3 MicroPython v2.0 or higher

# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3 = EV3Brick()
left_m = Motor(Port.B)
right_m = Motor(Port.A)
tower_m = Motor(Port.D)
print("1")
proxy = UltrasonicSensor(Port.S1)
print("2")
touch = TouchSensor(Port.S4)

ev3.speaker.beep()

def rotate_left_retarder(time):
    right_m.run_time(100, time, wait=False, then=Stop.HOLD)
    left_m.run_time(-100, time, then=Stop.HOLD)

def rotate_right_retarder(time):
    right_m.run_time(-100, time, wait=False, then=Stop.HOLD)
    left_m.run_time(100, time, then=Stop.HOLD)

def get_ratio2(tra):
    coe = 0.02
    dis = proxy.distance()
    if dis > 1000: 
        dis = 0
    ratio = 1 / (1 + pow(e, (-coe * (dis - tra))))
    return round(ratio * 1000) / 1000

def fw_bezpecne_bez_tower(time, tra): # pouze na konec
    c = 0
    while c < time:
        ratio = get_ratio2(tra)
        left_m.run(500 * (ratio) + 250)
        right_m.run(500 * (1 - ratio) + 250)
        sleep(0.1)
        c += 0.1
        print(proxy.distance())
        print(ratio)
    left_m.stop()
    right_m.stop()

def fw_bezpecne_s_tower(time, tra):
    c = 0
    pull_count = 0
    down = True
    while c < time:
        # ratio
        ratio = get_ratio2(tra)
        left_m.run(500 * (ratio) + 200)
        right_m.run(500 * (1 - ratio) + 200)
        # hand
        print(pull_count)
        if (pull_count == 0 and tower_m.angle() >= 735) or (pull_count > 0 and tower_m.angle() >= 735):
            if down == True:
                pull_count += 1
            down = False
        if tower_m.angle() <= 10:
            down = True
        if down:
            if pull_count == 0:
                tower_m.run_target(1200, 740, wait=False)
            else:
                tower_m.run_target(1200, 740, wait=False)
        else:
            if pull_count >= 4:
                tower_m.run_target(300, 0, wait=False)
            else:
                tower_m.run_target(300, 0, wait=False)
        sleep(0.1)
        c += 0.1

        print(pull_count)
    left_m.stop()
    right_m.stop()

def fw_bezpecne_s_tower_3_state(time, tra):
    state = "down" # "up" "waiting"
    c = 0
    wait = 0
    pull_count = 0
    while c < time:
        # getting ration
        ratio = get_ratio2(tra)
        left_m.run(500 * (ratio) + 200)
        right_m.run(500 * (1 - ratio) + 200)
        # state functions
        if state == "down":
            tower_m.run_target(1000, 770, wait=False)
            if tower_m.angle() >= 760:
                state = "up"
                pull_count += 1
        elif state == "up":
            tower_m.run_target(1000, 0, wait=False)
            if tower_m.angle() <= 5:
                state = "waiting"
                if pull_count == 4:
                    state = "lol"
        elif state == "waiting":
            wait += 0.01
            if wait > 0.5:
                wait = 0
                state = "down"
        else:
            print("lol, we are screwed")
        sleep(0.01)
        c += 0.01
    left_m.stop()
    right_m.stop()

def drive_straight(time, speed): 
    # kladná rychlost je dopředu
    left_m.run_time(speed, time, then=Stop.HOLD, wait=False)
    right_m.run_time(speed, time, then=Stop.HOLD, wait=True)



while not touch.pressed():
    print(proxy.distance())
    pass

tower_m.reset_angle(0)

# start a prvni rada
fw_bezpecne_s_tower_3_state(8.35, 55)
# otoceni pred 2. radou
rotate_left_retarder(1400)
drive_straight(1000, 750)
rotate_left_retarder(1600)
# druha rada
fw_bezpecne_bez_tower(2.3, 200)
fw_bezpecne_s_tower_3_state(6, 200)
tower_m.run_target(750, 500)
tower_m.run_target(0, 500)
# otoceni pred 3. radou
drive_straight(2000, -500)
rotate_left_retarder(4200)
drive_straight(4000, 1000)
tower_m.run_target(1000, 900, wait=False)
drive_straight(4000, -500)


# 3. rada
#fw_bezpecne_bez_tower(2, 55)
#fw_bezpecne_s_tower_3_state(8.35, 55)


#while True:
#    ev3.speaker.play_file("sexLoud.wav")
