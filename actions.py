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
    enable_servos()
    set_servo_position(c.servoCog, c.cogStart)
    set_servo_position(c.servoIgus, c.cogStart-500)
    set_servo_position(c.servoClaw, c.clawStart)
    '''motor(c.cogMotor, -50)
    msleep(1400)
    motor(c.cogMotor, 0)
    msleep(1000)'''


def turnToRing():
    drive_timed(200, 200, 750)
    drive_timed(200, -200, 700)
    moveCog(95, 1175)
    set_servo_position(c.servoIgus, c.cogGrab)
    drive_timed(-60, -200, 1700)

def liftRing():
    moveServo(c.servoIgus, c.cogStart - 450, 5)
    moveCog(100, 2000)
    moveServo(c.servoIgus, c.cogStart - 650, 5)

def makeTurn():
    #Continues up with the ring, turning so it does not hit the blocks
    #Right now the robot is very close to the blocks (though not touching)
    #Improve this!!
    motor(c.cogMotor, 100)
    drive_timed(-50, -75, 2000)
    motor(c.cogMotor, 0)
    drive_timed(-75, -50, 2000)
    moveCog(100, 1000)
    moveServo(c.servoIgus, c.cogStart - 850, 5)
    drive_timed(-75, -75, 1000)
    moveCog(100, 600)
    drive_timed(-75, -75, 2500)

def dropRing():
    #This drops the ring on the highest rung
    #Method works usually, but occasionally the Igus chain curls up, and the chain gets stuck
    #A better method of removing the Igus arm should be made!!!
    moveServo(c.servoIgus, c.cogStart - 650, 5)
    moveCog(-100, 500)
    drive_timed(-50, 50, 1000)
    moveServo(c.servoIgus, c.cogStart - 300, 5)
    moveCog(-100, 4500)

def slideTram():
    #Depends on position after drop, so may need to be changed as drop method changes
    drive_timed(200,140,1700)
    drive_timed(-185,185,2150)
    moveServo(c.servoClaw, c.clawTram, 10)
    drive_timed(150,150,875)
    drive_timed(100, 0, 4000)
    drive_timed(100, 100, 4000)

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
    motor(c.cogMotor, 50)
    msleep(500)
    #timedLineFollow(1)

def startDriving():
    drive_timed(100, 100, 1000)
    moveServo(c.servoCog, 1100, 10)
    rotate_degrees(-20, 100)
    drive_timed(-100, -100, 1000)
    driveAndLift(750)
    msleep(1000)
    lineFollowAndLift()
    DEBUG()




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
    drive_timed(-100, -100, 2000)
    moveServo(c.servoArm, c.armup, 10)
    msleep(2000)
    moveServo(c.servoArm, 1420, 10)
    drive_timed(100,100,2000)
    DEBUG()



