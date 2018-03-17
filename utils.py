import constants as c

from wallaby import *

def wait_for_button(force=False):
    if c.ALLOW_BUTTON_WAIT or force:
        print "Press Button..."
        while not right_button():
            pass
        msleep(1)
        print "Pressed"
        msleep(1000)

def DEBUG(PrintTime=True):
    create_drive_direct(0, 0)
    ao()
    create_safe()
    msleep(100)
    create_disconnect()
    if PrintTime:
        print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    disable_servos()
    exit(0)


def EXIT():
    create_drive_direct(0, 0)
    ao()
    create_safe()
    msleep(100)
    create_disconnect()
    print 'Program finished!\nSeconds: ', seconds() - c.START_TIME
    exit(0)


def DEBUG_with_wait():
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    msleep(5000)
    DEBUG(False)

def moveServo(servo, endPos, speed):
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if now > 2048:
        print("Servo setting too large ", servo)
    if now < 0:
        print("Servo setting too small ", servo)
    if now > endPos:
        speed = -speed
    for i in range(now, endPos, speed):
        set_servo_position(servo, i)
        msleep(10)
    set_servo_position(servo, endPos)
    msleep(10)

# def moveArm(servoMain, servoAssist, endPos, speed):
#     # speed of 1 is slow
#     # speed of 2000 is fast
#     # speed of 10 is the default
#     now = get_servo_position(servoMain)
#     if now > 2048:
#         print("Servo setting too large ", servoMain)
#     if now < 0:
#         print("Servo setting too small ", servoMain)
#     if now > endPos:
#         speed = -speed
#     for i in range(now, endPos, speed):
#         if c.IS_ORANGE_BOT:
#             x = int(2043.45 - 0.987 * (i))
#         elif c.IS_BLUE_BOT:
#             x = int(1924.48 - 0.987 * (i))
#         else:
#             x = int(1906.8 - 0.976 * (i)) #Previous values
#         set_servo_position(servoMain, i)
#         set_servo_position(servoAssist, x)
#         msleep(10)
#     set_servo_position(servoMain, endPos)
#     msleep(10)


def moveArm(endPos, speed):
    if get_motor_position_counter(c.leftMotor) > endPos:
        speed = -speed
        motor(c.leftMotor, speed)
        motor(c.rightMotor, speed)
        while get_motor_position_counter(c.leftMotor) > endPos:
            pass
    else:
        motor(c.leftMotor, speed)
        motor(c.rightMotor, speed)
        while get_motor_position_counter(c.leftMotor) < endPos:
            pass
    motor(c.leftMotor, 0)
    motor(c.rightMotor, 0)

def resetArm(time):
    #drive both motors to full-up positon
    motor(c.leftMotor, 40)
    motor(c.rightMotor, 40)
    msleep(time)
    ao()
    msleep(1000)
    clear_motor_position_counter(c.leftMotor)
    clear_motor_position_counter(c.rightMotor)


def testArm():
    print("left motor up")
    motor(c.leftMotor, 40)
    msleep(500)
    motor(c.leftMotor, 0)
    print("holding with left motor")
    msleep(1000)
    ao()
    msleep(1000)
    print("right motor up")
    motor(c.rightMotor, 40)
    msleep(500)
    motor(c.rightMotor, 0)
    print("holding with right motor")
    msleep(1000)
    ao()
    msleep(1000)
    #resetArm()




def igusReset():
    return digital(c.IGUS_BUTTON)