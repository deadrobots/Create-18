from wallaby import digital


FRONT_BUMPED = 0
ALLOW_BUTTON_WAIT = True
START_TIME = 0






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
ROBOT_ID_YELLOW = 0
ROBOT_ID_BLUE = 1
IGUS_BUTTON = 9

IS_YELLOW_BOT = digital(ROBOT_ID_YELLOW)
IS_BLUE_BOT = digital(ROBOT_ID_BLUE)
IS_ORANGE_BOT = not IS_BLUE_BOT and not IS_YELLOW_BOT



if IS_ORANGE_BOT:

    #Arm Servo Values
    armStartbox = 400  # 520 #2017
    armBotguy = 570
    armLow = 650
    armSandwich = 720
    armOut = 800
    armHorizontal = 900
    armUp = 1200
    armHigh = 1500
    armVeryHigh = 1700

    #Claw Servo Values
    clawClosed = 0
    clawMid = 100
    clawTram = 600 #Position to move tram
    clawOpen = 1065
    clawStart = 1730 #All the way back

    #Cog Servo Values
    cogRingDrop = 1100
    cogStartBox = 1200
    cogPegTwo = 1350
    cogStart = 1650 #was 1550
    cogGrab = 1800 #was 1780

elif IS_BLUE_BOT:
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
    cogRingDrop = 225  # was 250
    cogStartBox = 350
    cogPegTwo = 500  # was 600
    cogStart = 800 #was 900
    cogGrab = 980
