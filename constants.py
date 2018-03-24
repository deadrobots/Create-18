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
    armHigh = -290
    armBotguyDelivery = -355
    armScore = -400
    armDelivery = -415
    armUp = -440
    armSlightlyUp = -600
    armBotguyLift = -613
    armSandwich = -620
    armBotguy = -650
    armBotguyPickUp = -680
    armStartbox = -700



elif IS_BLUE_BOT:
    #Servo Ports
    servoClaw = 1
    servoIgus = 0

    INCHES_TO_TICKS = 560

    #Arm Servo Values
    armStartbox = 250
    armBotguy = 420
    armLow = 500
    armOut = 650
    armSandwich = 665
    armHorizontal = 750
    armUp = 1050
    armHigh = 1350
    armVeryHigh = 1550

    #Claw Servo Values
    clawClosed = 230
    clawTram = 950  # Position to move tram
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
    armHigh = -290
    armBotguyDelivery = -355
    armScore = -400
    armDelivery = -415
    armUp = -440
    armSlightlyUp = -600
    armBotguyLift = -613
    armSandwich = -620
    armBotguy = -650
    armBotguyPickUp = -680
    armStartbox = -700
