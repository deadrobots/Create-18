from wallaby import *
from math import pi
from utils import *
import constants as c


def drive_timed(left, right, time):
    create_drive_direct(-right, -left)
    msleep(time)
    create_drive_direct(0, 0)


def spin_cw(power, time):
    create_drive_direct(power, -power)
    msleep(time)
    create_drive_direct(0, 0)


def spin_ccw(power, time):
    create_drive_direct(-power, power)
    msleep(time)
    create_drive_direct(0, 0)


def rotate(power, time):
    if power > 0:
        spin_ccw(power, time)
    else:
        spin_cw(abs(power), time)


def split_drive(left, right, time, increments, turnTime):
    power = -100
    if turnTime < 0:
        turnTime = abs(turnTime)
        power = abs(power)
    if turnTime == 0:
        drive_timed(left, right, time)
    else:
        for _ in range(0, increments):
            drive_timed(left, right, int(time / increments))
            rotate(power, turnTime)


def split_drive_condition(left, right, min, time, turnTime, condition, state=True):
    start = seconds() + time
    create_drive_direct(-left, -right)
    msleep(min)
    while condition() is state:
        current = seconds()
        if current > start:
            print turnTime
            start = current + time
            rotate(-100, turnTime)
            create_drive_direct(left, right)
            msleep(min)
    create_drive_direct(0, 0)


def drive_conditional(left, right, testFunction, state=True):
    create_drive_direct(-right, -left)
    while testFunction() is state:
        pass
    stop()


def drive_forever(left, right):
    create_drive_direct(-right, -left)


def stop():
    create_stop()


INCH_TO_MIL = 25.4
def drive_distance(distance, speed):

    dist_mil = INCH_TO_MIL * distance
    time = dist_mil / speed
    drive_timed(speed, speed, time)


def rotate_degrees(degrees, speed):
    if degrees < 0:
        speed = -speed
        degrees = abs(degrees)
    degrees = degrees * 1.13
    set_create_total_angle(0)
    drive_forever(-speed, speed)
    while abs(get_create_total_angle()) < degrees:
        pass
    stop()

    # diameter_inch = 9
    # diameter_mil = diameter_inch * INCH_TO_MIL
    # if degrees < 0:
    #     speed = -speed
    #     degrees = -degrees
    # angle = abs(degrees / 360.0)
    # circ = pi * diameter_mil
    # drive_mil = angle * circ
    # time = drive_mil / speed
    # rotate(speed, time)


def drive_accel(speed, time):
    for sub_speed in range(0, speed+1, 100):
        create_drive_direct(-sub_speed, -sub_speed)
        msleep(100)
    msleep(time)
    create_drive_direct(0, 0)

def timedLineFollow(time):
    sec = seconds()
    while(seconds() - sec<time):
        if get_create_lfcliff_amt() < 2000:
            create_drive_direct(200, 150)
        else:
            create_drive_direct(150, 200)
    create_stop()

def lineFollowTilCrossBlack():
    while(get_create_lcliff_amt() > 2000):
        if get_create_lfcliff_amt() < 2000:
            create_drive_direct(200, 150)
        else:
            create_drive_direct(150, 200)
    while (get_create_lcliff_amt() < 2000):
        if get_create_lfcliff_amt() < 2000:
            create_drive_direct(200, 150)
        else:
            create_drive_direct(150, 200)
    create_stop()

def driveTilBlackLCliff(speed):
    create_drive_direct(speed, speed)
    while (get_create_lcliff_amt() > 2000):
        pass
    create_stop()

def driveTilBlackRCliff(speed):
    create_drive_direct(speed, speed)
    while (get_create_rcliff_amt() > 2000):
        pass
    create_stop()

def turnTilBlackLCliff(left, right):
    create_drive_direct(left, right)
    while (get_create_lcliff_amt() > 2000):
        pass
    create_stop()

def turnTilBlackRCliff(left, right):
    create_drive_direct(left, right)
    while (get_create_rcliff_amt() > 2000):
        pass
    create_stop()


def driveAcrossBlack(speed):
    create_drive_direct(speed, speed)
    while (get_create_lcliff_amt() > 2000):
        pass
    while (get_create_lcliff_amt() < 2000):
        pass
    msleep(100)
    create_stop()

def turnAcrossBlack(left, right):
    create_drive_direct(left, right)
    while (get_create_lfcliff_amt() > 2000):
        pass
    while (get_create_lfcliff_amt() < 2000):
        pass
    msleep(200)
    create_stop()

def driveUntilBlue(speed):
    create_drive_direct(speed, speed)
    while (get_create_rfcliff_amt() > 2000):
        pass
    create_stop()


def timedLineFollowLeft(time):
    sec = seconds()
    while(seconds() - sec<time):
        if get_create_lcliff_amt() < 2000:
            create_drive_direct(150, 100)
        else:
            create_drive_direct(100, 150)
    create_stop()


def lineFollowAndLift(time):
    sec = seconds()
    while (seconds() - sec < time):
        i = 0
        if i < 1:
            timedLineFollowLeft(.1)
            i += 1
        else:
            moveCog(50, 100)
            i += 1


def driveAndLift(time):
    drive_timed(-100, -100, time)
    moveCog(50, time)
    stop()


def moveCog(speed, time):
    motor(c.cogMotor, speed)
    msleep(time)
    motor(c.cogMotor, 0)

def resetChain():
    startTime = seconds()
    print 'retracting'
    motor(c.cogMotor, -100)
    while (seconds() - startTime < 10):
        if igusReset():
            freeze(c.cogMotor)
            print'stopping'
            break
    freeze(c.cogMotor)
    # resets based on motor forced stopping
    '''previousCount= 0
    clear_motor_position_counter(c.cogMotor)

    while (seconds() - startTime < 5):
        msleep(50)
        currentCount=get_motor_position_counter(c.cogMotor)
        print currentCount
        if previousCount-currentCount>=20:
            previousCount=currentCount
        else:
            freeze(c.cogMotor)
            print'stopping'
            break'''