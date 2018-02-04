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


def driveBotGuy():
    #Drives to center of board (avoiding pom piles) to point arm at BotGuy
    print ("driveBotGuy")
    drive_timed(250, 250, 600)
    drive_timed(-250, 250, 420)
    drive_timed(0, 0, 500)
    drive_timed(250, 250, 2700)
    wait_for_button(False)
    # Turns robot around so arm is facing center of board then positions to drive straight to BotGuy
    drive_timed(250, 150, 2700)
    wait_for_button(False)
    drive_timed(-250, 250, 1670)
    wait_for_button(False)
    drive_timed(-150, -150, 2100)
    wait_for_button(False)
    drive_timed(-250, -60, 2300)
    wait_for_button(False)
    #Drives forward to grab BotGuy
    drive_timed(98, 100, 2700)