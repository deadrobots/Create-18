#!/usr/bin/python
import os, sys
import actions as act
import constants as c
from wallaby import *
import utils as u
import movement as m

def main():
    print ("Running the code")
    #Code moves ring to top rung and then pushes the tram to the middle (usually)
    act.init()
    act.turnToRing()
    act.liftRing()
    u.DEBUG()
    act.raiseRing()
    act.dropRing()
    act.slideTram()
    act.approachCenter()
    u.DEBUG()
    #act.getOutOfSB()
    #act.raiseCog()
    #act.startDriving()
    #act.goToCenter()
    act.driveBotGuy()


    create_disconnect()
if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()