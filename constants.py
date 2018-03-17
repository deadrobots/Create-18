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

    servoArmMain = 2
    servoArmAssist = 3
    servoClaw = 1
    servoIgus = 0

    #Claw Servo Values
    clawClosed = 0
    clawFrisbeeTight = 95
    clawMid = 200
    clawTram = 600 #Position to move tram
    clawOpen = 1065
    clawStart = 1730 #All the way back

    #Cog Servo Values
    cogRingDrop = 1100
    cogStartBox = 1200
    cogPegTwo = 1350
    cogStart = 1650
    cogGrab = 1800
    cogLift = 1090
    cogLiftContinued = 770
    evenMoreCogLift = 980
    cogServoVeryHigh = 920

    #Old arm servo values
    # armStartbox = 530
    # armBotguy = 500
    # armLow = 650
    # armOut = 730
    # armSandwich = 745
    # armHorizontal = 830
    # armUp = 1130
    # armHigh = 1430
    # armVeryHigh = 1630
    # ##
    # armSlightlyUp = 760

    #current motor arm values
    armStartbox = -700
    armBotguy = 500
    armLow = 650
    armOut = 730
    armSandwich = 745
    armHorizontal = 830
    armUp = 1130
    armHigh = -310
    armSlightlyUp = 760
    armVeryHigh = -150


elif IS_BLUE_BOT:
    #Servo Ports
    servoArmMain = 2
    servoArmAssist = 3
    servoClaw = 1
    servoIgus = 0

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
    cogRingDrop = 215
    cogStartBox = 350
    cogPegTwo = 500
    cogStart = 800
    cogGrab = 980
    cogLift = 200
    cogLiftContinued = 75
    evenMoreCogLift = 25
    cogServoVeryHigh = 5
