import constants as c

from wallaby import *

def wait_for_button(force=False):
    if c.ALLOW_BUTTON_WAIT or force:
        print "Press Button..."
        while not right_button():
            pass
        msleep(1)
        print "Pressed"
        msleep(1000)

def DEBUG(PrintTime=True):
    create_drive_direct(0, 0)
    ao()
    create_safe()
    msleep(100)
    create_disconnect()
    if PrintTime:
        print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    exit(0)


def EXIT():
    create_drive_direct(0, 0)
    ao()
    create_safe()
    msleep(100)
    create_disconnect()
    print 'Program finished!\nSeconds: ', seconds() - c.START_TIME
    exit(0)


def DEBUG_with_wait():
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    msleep(5000)
    DEBUG(False)