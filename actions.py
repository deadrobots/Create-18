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
    if c.IS_ORANGE_BOT:
        print("I AM ORANGE")
    elif c.IS_BLUE_BOT:
        print("I AM BLUE")
    else:
        print("I AM YELLOW")
    selfTest()
    print("Press right button to continue")
    wait_for_button()
    print("Pressed.")
    c.START_TIME = seconds()

def selfTest():
    # raise arm
    enable_servo(c.servoArmMain)
    enable_servo(c.servoArmAssist)
    moveArm(c.servoArmMain, c.servoArmAssist, c.armHorizontal, 10)
    # open/close claw
    enable_servo(c.servoClaw)
    moveServo(c.servoClaw, c.clawClosed, 15)
    moveServo(c.servoClaw, c.clawStart, 15)
    # test drive
    drive_timed(100, 100, 2500)
    msleep(250)
    drive_timed(-100, -100, 2500)
    msleep(250)
    # lower ramp
    enable_servo(c.servoIgus)
    moveServo(c.servoIgus, c.cogStart - 300, 10)
    # move the chain
    moveCog(100, 1500)# enables cog
    resetChain()
    # raise ramp
    moveServo(c.servoIgus, c.cogStartBox, 10)
    msleep(250)
    # lower the arm
    moveArm(c.servoArmMain, c.servoArmAssist, c.armStartbox, 10)



def turnToRing():
    print ('Turn to ring')
    set_servo_position(c.servoArm,c.armUp)
    msleep(500)
    if c.IS_ORANGE_BOT:
        pass
    elif c.IS_BLUE_BOT:
        drive_timed(-100, -100, 250)
        drive_timed(100, 0, 1200)
    drive_timed(100, 100, 1700) #squares up to west wall
    if c.IS_ORANGE_BOT:
        drive_timed(-100, -85, 1300)
    elif c.IS_BLUE_BOT:
        drive_timed(-100, -95, 1500)
    drive_timed(-180, 180, 1000)
    drive_timed(100, 100, 1000) #1200
    set_servo_position(c.servoIgus, c.cogGrab)
    if c.IS_ORANGE_BOT:
        moveCog_position(3.5, 95)
    elif c.IS_BLUE_BOT:
        moveCog_position(2.8, 95)
    driveTilBlackLCliff(100)
    if c.IS_ORANGE_BOT:
        drive_timed(-30, -60, 900)
    elif c.IS_BLUE_BOT:
        drive_timed(-50, -50, 500)


def liftRing():
    if c.IS_ORANGE_BOT:
        moveServo(c.servoIgus, c.cogStart - 250, 5)
        moveCog_position(6, 100)
        moveServo(c.servoIgus, c.cogStart - 350, 5)
    elif c.IS_BLUE_BOT:
        moveServo(c.servoIgus, c.cogStart - 450, 5)
        moveCog_position(5.75, 100)
        moveServo(c.servoIgus, c.cogStart - 600, 5)
        timedLineFollowLeftFront(1)

def raiseRing2():
    # orange
    timedLineFollowLeftFront(1.9)
    moveServo(c.servoIgus, 1090, 5)
    moveCog_position(2.5, 100)
    timedLineFollowLeftFront(1.9)
    moveServo(c.servoIgus, 980, 5)
    moveCog_position(4, 100)
    lineFollowLeftFrontTilBlack()
    lineFollowLeftFrontTilWhite()
    moveServo(c.servoIgus, 920, 5)
    moveCog_position(1.5, 100)
    timedLineFollowLeftFront(1.8)

def raiseRing():
    if c.IS_ORANGE_BOT:
        motor(c.cogMotor, 100)
        moveServo(c.servoIgus, c.cogStart - 620, 5)
        timedLineFollowLeftFront(2.2) #was 1.6
        motor(c.cogMotor, 0)
        moveServo(c.servoIgus, c.cogStart - 640, 5)
        timedLineFollowLeftFront(1) #was 1.6
    elif c.IS_BLUE_BOT:
        motor(c.cogMotor, 100)
        moveServo(c.servoIgus, c.cogStart - 610, 5)
        timedLineFollowLeftFront(2.2)  # was 1.6
        motor(c.cogMotor, 0)
        moveServo(c.servoIgus, c.cogStart - 650, 5)
        timedLineFollowLeftFront(1)  # was 1.6
    DEBUG()
    if c.IS_ORANGE_BOT:
        moveServo(c.servoIgus, 770,5)
    elif c.IS_BLUE_BOT:
        moveServo(c.servoIgus, c.cogRingDrop-150, 5)
        motor(c.cogMotor, 100)
    # timedLineFollowLeftFront(.75)
    lineFollowLeftFrontTilBlack()
    motor(c.cogMotor, 0)
    if c.IS_ORANGE_BOT:
        moveCog_position(5, 50)
    elif c.IS_BLUE_BOT:
        #moveCog_position(5.5, 50)
        pass
    lineFollowLeftFrontTilWhite()
    timedLineFollowLeftFront(.5)

def dropRing():
    moveCog_position(-5, 100)
    moveServo(c.servoIgus, c.cogRingDrop, 5)
    moveCog_position(-1, 100)
    msleep(500) #do not remove: keep so ring frisbee stops swinging
    drive_timed(-50, 50, 1200)
    moveServo(c.servoIgus, c.cogStart-300, 3)
    resetChain()
    moveServo(c.servoIgus, c.cogRingDrop, 5)

def slideTram():
    #Depends on position after drop, so may need to be changed as drop method changes
    #tram keeps getting stuck on the claw pegs - need to work on sliding it without getting stuck
    moveServo(c.servoClaw, c.clawClosed, 20)
    moveServo(c.servoArm, c.armVeryHigh, 10)
    if c.IS_ORANGE_BOT:
        drive_timed(100,100,1300)
    rotate_degrees(-165, 100)
    moveServo(c.servoArm, c.armHigh, 5)
    drive_timed(100, 100, 200)
    rotate_degrees(-75, 100)
    drive_timed(100, 100, 1600) #shorter drive
    rotate_degrees(-25, 100) #tram gets stuck during this rotate
    #drive_timed(100, 100, 1900) #shorter
    #wait_for_button()
    #rotate_degrees(-24, 100)
    driveTilBlackLCliffAndSquareUp(-100)
    drive_timed(100, 100, 1100)

def approachCenter():
    rotate_degrees(90, 100)
    drive_timed(100,100,1900)
    driveTilBlackLCliffAndSquareUp(100)
    msleep(1000)
    drive_timed(-100,-100, 6350)
    drive_timed(90, -90, 2000)
    moveServo(c.servoArm, c.armVeryHigh, 5)
    drive_timed(150, 150, 1500)
    drive_timed(50, 50, 2300)


def getFrisbee():
    #Goal is to grab date tree frisbees and make a date sanwich
    #Then back up and deposit your fresh date sandwich into the tram bin
    driveTilBlackLFCliff(100)
    driveTilWhiteLFCliff(100)
    # moveServo(c.servoArm, c.armVeryHigh, 15)
    moveServo(c.servoClaw, c.clawOpen, 15)
    # drive_timed(-150, -150, 1600)
    # msleep(1000)
    # rotate_degrees(-25, 150)
    moveServo(c.servoArm, c.armSandwich, 15)
    driveTilBlackLFCliff(-100)
    driveTilWhiteLFCliff(-100)
    drive_timed(100,100, 150)
    moveServo(c.servoClaw, c.clawMid, 15)
    msleep(1000)
    moveServo(c.servoArm, c.armSlightlyUp, 2)
    moveServo(c.servoClaw, c.clawFrisbeeTight,2)
    moveServo(c.servoArm, c.armUp, 2)
    driveTilBlackLCliffAndSquareUp(100)
    rotate_degrees(53, 50)
    moveServo(c.servoArm, c.armHigh, 7)
    #This drive isn't straight on
    drive_timed(100, 100, 2700)#50,50,5800
    wait_for_button()
    moveServo(c.servoClaw, c.clawOpen, 5)
    DEBUG()
    drive_timed(-50, -50, 2000)
    moveServo(c.servoClaw, c.clawClosed, 5)
    DEBUG()

#test functions
#not used, placed out of the way

def goToCenter():
    #Create line follows to middle then goes to right of center area to reach Botguy
    lineFollowTilCrossBlack()
    timedLineFollow(.85)
    set_servo_position(c.servoClaw, c.clawClosed)
    wait_for_button()
    #drive_timed(150, -250, 1000)
    #msleep(2000)
    #drive_timed(0, 600, 300)
    #msleep(3000)
    #drive_timed(0, -600, 300)
    drive_timed(150, -250, 900)
    moveServo(c.servoArm , c.armHorizontal, 5)
    drive_timed(75,75,500)
    set_servo_position(c.servoClaw, c.clawOpen)
    msleep(600)
    drive_timed(150, -250, 1500)
    drive_timed(75, 75, 4000)
    drive_timed(75, -175, 400)
    drive_timed(-75, -75, 500)
    drive_timed(75, 75, 2500)
    set_servo_position(c.servoClaw, c.clawClosed)
    msleep(500)
    set_servo_position(c.servoClaw, c.clawOpen)
    driveTilBlackRCliff(150)
    turnTilBlackLCliff(100, 0)
    drive_timed(-130, -130, 800)
    set_servo_position(c.servoArm, c.armHigh)

    msleep(500)
    drive_timed(-100, -100, 2000)
    moveServo(c.servoArm, c.armUp, 10)
    msleep(2000)
    moveServo(c.servoArm, 1420, 10)
    drive_timed(100, 100, 2000)
    DEBUG()