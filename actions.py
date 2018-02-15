from movement import *
from utils import *
import constants as c
from wallaby import *


def init():
    '''For Setup:
    Make sure that both bumpers are touching the back edges of the starting box
    Point the "arm" at the opposite corner of starting box (intersection of black tape)
    Use pencil marks on table to check alignment
    Line up the block of wood with the straight line to perfect the setup'''
    create_disconnect()
    if not create_connect_once():
        print("Create not connected...")
        exit(0)
    print("Create connected...")
    create_full()

def getOutOfSB():
    #Gets Create out of start box and ready to line follow
    print "Push left button to end"
    enable_servos()
    moveServo(c.servoArm, c.armup, 20)
    moveServo(c.servoClaw, c.clawMiddle, 10)
    drive_timed(80,80, 2000)
    rotate_degrees(55, 70)
    #drive_timed(100, 100, 1000)
    rotate_degrees(-150,50)
    timedLineFollow(3.3)


def driveToCenter():
    rotate_degrees(80,70)
    driveTilBlackRCliff(-150)
    turnTilBlackLCliff(-100, 0)
    drive_timed(150,150, 5000)
    drive_timed(-100, -100, 1500)
    rotate_degrees(53, 70)
    drive_timed(-100,-100,500)
    moveServo(c.servoArm, c.armLow, 10)

def getBotguy():
    drive_timed(100,100,1000)
    moveServo(c.servoClaw, c.clawOpen, 10)
    moveServo(c.servoArm, c.armBotguy, 10)
    drive_timed(100,100, 1500)
    moveServo(c.servoClaw, c.clawClosed, 10)
    msleep(2000)
    moveServo(c.servoArm, c.armOut, 10)
    msleep(500)
    drive_timed(-100, -100, 2000)
    moveServo(c.servoArm, c.armup, 10)
    msleep(2000)






