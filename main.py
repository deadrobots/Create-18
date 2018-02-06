#!/usr/bin/python
import os, sys
import actions as act
import constants as c
from wallaby import *


def main():
    act.init()
    print ("Turn create on!!!!")
    act.getOutOfSB()
    act.goToCenter()
    #act.driveBotGuy()

    create_disconnect()
if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()