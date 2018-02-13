#!/usr/bin/python
import os, sys
import actions as act
import constants as c
from wallaby import *
import utils as u
from movement import *


def main():
    print ("Running")
    act.init()
    lineFollowAndLift(5)
    DEBUG()

    act.getOutOfSB()
    act.raiseCog()
    act.startDriving()

    #act.goToCenter()
    #act.driveBotGuy()

    create_disconnect()
if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()