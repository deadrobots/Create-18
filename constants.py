from wallaby import digital


FRONT_BUMPED = 0
ALLOW_BUTTON_WAIT = True
START_TIME = 0

CLONE_SWITCH = 0
IS_CLONE = digital(CLONE_SWITCH)
IS_PRIME = not IS_CLONE

#Motor Ports
cogMotor = 3

# Drive Info
TURN_TIME = 0  # -20  # 0, 15, 40


LOGFILE = "" # Leave empty
ROBOT_NAME = "Create-17"


#Servo ports for blue Create
#servoClaw = 3
#servoCog = 1

#Servo ports for red Create
servoArm = 0
servoClaw = 2
servoIgus = 3

# Digital ports
IGUS_BUTTON = 9

if IS_PRIME:

    #Arm Servo Values
    armStartbox = 400  # 520 #2017
    armBotguy = 570
    armLow = 650
    armOut = 800
    armHorizontal = 900
    armUp = 1200
    armHigh = 1500
    armVeryHigh = 1700

    #Claw Servo Values
    clawClosed = 0
    clawTram = 600 #Position to move tram
    clawOpen = 1065
    clawStart = 1730 #All the way back

    #Cog Servo Values
    cogRingDrop = 900
    cogStartBox = 800
    cogPegTwo = 1000
    cogStart = 1700
    cogGrab = 1780

else:
    #Arm Servo Values
    armStartbox = 250  # 2017
    armBotguy = 470
    armLow = 550
    armOut = 700
    armHorizontal = 800
    armUp = 1100
    armHigh = 1400
    armVeryHigh = 1700

    #Claw Servo Values
    clawClosed = 230
    clawTram = 950  # Position to move tram
    clawOpen = 1400
    clawStart = 2047 #All the way back

    #Cog Servo Values
    cogStartBox = 0
    cogRingDrop = 225 #was 250
    cogPegTwo = 500  # was 600
    cogStart = 800 #was 900
    cogGrab = 980
