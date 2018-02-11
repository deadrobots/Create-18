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
    '''motor(c.cogMotor, -50)
    msleep(1400)
    motor(c.cogMotor, 0)
    msleep(1000)'''

def getOutOfSB():
    #Gets Create out of start box and ready to line follow
    print "Push left button to end"
    enable_servos()
    set_servo_position(c.servoCog, c.cogStart)
    motor(c.cogMotor, 50)
    msleep(2500)
    motor(c.cogMotor, 0)
    #moveServo(c.servoArm, c.armup, 20)
    driveTilBlackRCliff(-250)
    turnTilBlackLCliff(150, 0)
    drive_timed(0, -150, 370)
    msleep(500)
    '''motor(c.cogMotor, -50)
    msleep(1050)
    motor(c.cogMotor, 0)'''
    #drive_timed(-250, -250, 1000)

def raiseCog():
    moveServo(c.servoCog, 1300, 10)
    DEBUG()
    motor(c.cogMotor, 50)
    msleep(500)
    timedLineFollow(1)


def goToCenter():
    #Create line follows to middle then goes to right of center area to reach Botguy
    lineFollowTilCrossBlack()
    timedLineFollow(.85)
    set_servo_position(c.servoClaw, c.clawClosed)
    #drive_timed(150, -250, 1000)
    #msleep(2000)
    #drive_timed(0, 600, 300)
    #msleep(3000)
    #drive_timed(0, -600, 300)
    drive_timed(150, -250, 900)
    set_servo_position(c.servoArm, 819)
    drive_timed(-75,-75,500)
    set_servo_position(c.servoClaw, c.clawOpen)
    msleep(600)
    drive_timed(150, -250, 1500)
    drive_timed(75,75,4000)
    drive_timed(75, -175, 400)
    drive_timed(-75, -75, 500)
    drive_timed(75,75,2500)
    set_servo_position(c.servoClaw, c.clawClosed)
    msleep(500)
    set_servo_position(c.servoClaw, c.clawOpen)
    driveTilBlackRCliff(150)
    turnTilBlackLCliff(100, 0)
    drive_timed(-130, -130, 800)
    set_servo_position(c.servoArm, c.armHigh)
    msleep(500)
    drive_timed(150, -250, 500)
    drive_timed(150, 150, 4000)
    drive_timed(-130, 130, 500)
    drive_timed(90, 90, 3500)
    drive_timed(-150, 0, 2300)
    drive_timed(150, 150, 1500)
    drive_timed(100, 0, 1000)
    DEBUG()
    '''
    set_servo_position(c.servoArm, c.armup)
    drive_timed(0, -165, 1870)
    set_servo_position(c.servoArm, c.armOut)
    drive_timed(135, 135, 500)
    drive_timed(90, 90, 700) #130, 160
    set_servo_position(c.servoClaw, 1611)
    drive_timed(-100,-100, 1000)
    drive_timed(150, 250, 850) #100, 100
    #set_servo_position(c.servoArm, c.armup)
    drive_timed(-150, -150, 750)
    drive_timed(-155, 0, 750)
    drive_timed(100, 100, 1500)'''

   # drive_timed(-150, -250, 2000)

    """wait_for_button(False)
    while get_create_lcliff_amt() > 2000:
        create_drive_direct(250, 150)
    create_stop
    drive_timed(-250, -150, 1500)
    drive_timed(-200, -200, 500)"""

