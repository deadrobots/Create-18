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
    if c.IS_CLONE:
        print("I AM CLONE")
    elif c.IS_PRIME:
        print("I AM PRIME")
    else:
        print("I DON'T KNOW WHAT I AM")
    selfTest()
    print("Press right button to continue")
    wait_for_button()
    print("Pressed.")
    c.START_TIME = seconds()

def selfTest():
    enable_servo(c.servoArm)
    moveServo(c.servoArm, c.armHorizontal, 10)
    enable_servo(c.servoClaw)
    moveServo(c.servoClaw, c.clawClosed, 15)
    moveServo(c.servoClaw, c.clawStart, 15)
    drive_timed(-100, -100, 750)
    drive_timed(0, 0, 250)
    drive_timed(100, 100, 750)
    drive_timed(0, 0, 0)
    moveServo(c.servoArm, c.armStartbox, 10)
    msleep(250)
    enable_servo(c.servoIgus)
    moveServo(c.servoIgus, c.cogGrab, 10)
    moveServo(c.servoIgus, c.cogPegTwo, 10)
    msleep(250)
    moveCog(100, 1500)
    resetChain()

def turnToRing():
    print ('Turn to ring')
    set_servo_position(c.servoArm,c.armUp)
    msleep(1000)
    drive_timed(-100, -100, 250)
    drive_timed(100, 0, 1200)
    drive_timed(100, 100, 1700) #squares up to west wall
    if c.IS_PRIME:
        drive_timed(-100, -85, 1300)
    else:
        drive_timed(-100, -95, 1500)
    drive_timed(-180, 180, 1000)
    drive_timed(100, 100, 1200)
    set_servo_position(c.servoIgus, c.cogGrab)
    moveCog_position(2.8, 95)
    msleep(1000)
    drive_timed(-50, -50, 4000)

def liftRing():
    if c.IS_PRIME:
        moveServo(c.servoIgus, c.cogStart - 450, 5)
        moveCog_position(5, 100)
        moveServo(c.servoIgus, c.cogPegTwo, 5)
    else:
        moveServo(c.servoIgus, c.cogStart - 450, 5)
        moveCog_position(5.75, 100)
        moveServo(c.servoIgus, c.cogStart - 600, 5)
    timedLineFollowLeftFront(1)

def raiseRing():
    motor(c.cogMotor, 100)
    timedLineFollowLeftFront(1.7)
    motor(c.cogMotor, 0)
    timedLineFollowLeftFront(1.7)
    if c.IS_PRIME:
        moveServo(c.servoIgus,c.cogRingDrop,5)
    else:
        moveServo(c.servoIgus, c.cogRingDrop-150, 5)
    timedLineFollowLeftFront(.75)
    if c.IS_PRIME:
        moveCog_position(4,50)
    else:
        moveCog_position(5.5, 50)
    timedLineFollowLeftFront(1.4)

def dropRing():
    moveCog_position(-5, 100)
    moveServo(c.servoIgus, c.cogRingDrop, 5)
    moveCog_position(-2, 100)
    drive_timed(-50, 50, 1200)
    moveServo(c.servoIgus, c.cogStart-300, 3)
    resetChain()

def slideTram():
    #Depends on position after drop, so may need to be changed as drop method changes
    moveServo(c.servoClaw, c.clawClosed, 20)
    moveServo(c.servoArm, c.armVeryHigh, 10)
    rotate_degrees(-165, 100)
    moveServo(c.servoArm, c.armHigh, 5)
    rotate_degrees(-75, 100)
    drive_timed(100, 100, 1250) #shorter drive
    rotate_degrees(-25, 100)
    drive_timed(100, 100, 2000) #shorter
    rotate_degrees(50, 100)
    drive_timed(-100, -100, 3000)
    turnAcrossBlack(-50,-100)
    rotate_degrees(15, 20)
    drive_timed(-100, -100, 2000)
    rotate_degrees(-90,75)
    drive_distance(9,100)
    #drive_timed(75, 100, 2500)
    DEBUG()

    drive_timed(-100, -100, 2500)
    moveServo(c.servoClaw, c.clawTram, 10)
    drive_timed(100,200,1900)
    drive_timed(100, 0, 4000)
    drive_timed(100, 100, 4300)
    wait_for_button()

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
    drive_timed(-100, -100, 2000)
    moveServo(c.servoArm, c.armUp, 10)
    msleep(2000)
    moveServo(c.servoArm, 1420, 10)
    drive_timed(100,100,2000)
    DEBUG()

    #functions not used
    #placed out of way
def getOutOfSB():
    #Gets Create out of start box and ready to line follow
    print "Push left button to end"
    enable_servos()
    set_servo_position(c.servoArm, c.cogStart)
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
    moveServo(c.servoArm, 1300, 10)
    motor(c.cogMotor, 50)
    msleep(500)
    #timedLineFollow(1)

def startDriving():
    drive_timed(100, 100, 1000)
    moveServo(c.servoArm, 1100, 10)
    rotate_degrees(-20, 100)
    drive_timed(-100, -100, 1000)
    driveAndLift(750)
    msleep(1000)
    lineFollowLeftAndLift()
    DEBUG()




