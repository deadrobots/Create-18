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
servoArm = 1
servoClaw = 2
servoIgus = 3

if IS_PRIME:

    #Arm Servo Values
    armOut = 800
    armup = 1200
    armStartbox = 520 #2017
    armHigh = 1500
    armLow = 650
    armBotguy = 570

    #Claw Servo Values
    clawOpen = 1065
    clawClosed = 0
    clawTram = 600 #Position to move tram
    clawStart = 1730 #All the way back

    #Cog Servo Values
    cogStartBox=800
    cogStart = 1700
    cogPegTwo = 1400
    cogGrab = 1780

else:
    #Arm Servo Values
    armOut = 700
    armup = 1100
    armStartbox = 250 #2017
    armHigh = 1400
    armLow = 550
    armBotguy = 470

    #Claw Servo Values
    clawOpen = 1400
    clawClosed = 230
    clawTram = 950 #Position to move tram
    clawStart = 2047 #All the way back

    #Cog Servo Values
    cogStartBox=0
    cogStart = 800 #was 900
    cogPegTwo = 500 #was 600
    cogGrab = 980
