#!/usr/bin/python
import os, sys
import actions as act
import constants as c
from wallaby import *
import utils as u


def main():
    act.init()
    print ("Turn create on!!!!")
    act.getOutOfSB()
    act.goToCenter()
    act.grabBotguy()


    create_disconnect()
if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()