from wallaby import digital


FRONT_BUMPED = 0
ALLOW_BUTTON_WAIT = True
START_TIME = 0

#Motor Ports
leftMotor = 0
rightMotor = 2
cogMotor = 3

# Drive Info
TURN_TIME = 0

LOGFILE = "" # Leave empty
ROBOT_NAME = "Create-17"

# Digital ports
ROBOT_ID_YELLOW = 0
ROBOT_ID_BLUE = 1
IGUS_BUTTON = 9

IS_YELLOW_BOT = digital(ROBOT_ID_YELLOW)
IS_BLUE_BOT = digital(ROBOT_ID_BLUE)
IS_ORANGE_BOT = not IS_BLUE_BOT and not IS_YELLOW_BOT


if IS_ORANGE_BOT:

    servoClaw = 1
    servoIgus = 0

    INCHES_TO_TICKS = 600

    #Claw Servo Values
    clawClosed = 0
    clawFrisbeeTight = 397
    clawMid = 517
    clawBotguy = 650 #was 717
    clawGrabBG = 817
    clawTram = 917 #Position to move tram
    clawOpen = 1382
    clawStart = 2047 #All the way back; used to be 1730

    #Cog Servo Values
    cogLiftContinued = 770
    cogServoVeryHigh = 920
    evenMoreCogLift = 980
    cogLift = 1090
    cogRingDrop = 1100
    cogStartBox = 1200
    cogPegTwo = 1350
    cogStart = 1650
    cogGrab = 1725

    #current motor arm values
    armVeryHigh = -150
    armTram = -285
    armHigh = -290
    armBotguyDelivery = -160 #was -355
    armScore = -400
    armDelivery = -415
    armUp = -440
    armSlightlyUp = -600
    armBotguyLift = -613
    armSandwich = -620
    armBotguy = -590
    armBotguyPickUp = -615
    armStartbox = -700



elif IS_BLUE_BOT:
    #Servo Ports
    servoClaw = 1
    servoIgus = 0

    INCHES_TO_TICKS = 560



    #Claw Servo Values
    clawClosed = 230
    clawMid = 550
    clawBotguy = 650
    clawGrabBG = 750
    clawTram = 900  # Position to move tram
    clawOpen = 1400
    clawStart = 2047 #All the way back

    #Cog Servo Values
    cogServoVeryHigh = 5
    evenMoreCogLift = 25
    cogLiftContinued = 75
    cogLift = 200
    cogRingDrop = 215
    cogStartBox = 350
    cogPegTwo = 500
    cogStart = 800
    cogGrab = 800

    #current motor arm values
    armVeryHigh = -150
    armTram = -285
    armHigh = -290
    armBotguyDelivery = -320
    armScore = -370
    armDelivery = -385
    armUp = -410
    armSlightlyUp = -570
    armBotguyLift = -585
    armSandwich = -595
    armBotguy = -625
    armBotguyPickUp = -650
    armStartbox = -700
