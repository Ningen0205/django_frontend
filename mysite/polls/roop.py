import nfc
import binascii
import os
import RPi.GPIO as GPIO
import time

roop_flg = False
path = f"{os.getcwd()}/allowCardLists.txt"

with open(path) as f:
    cards = f.readlines()
    cards = [i.replace('\n','') for i in cards]

def connected(tag):
    idm = binascii.hexlify(tag.idm).decode('utf-8')
    print(idm)
    for card in cards:
        card.encode('utf-8')
        if card == idm:
            GPIO.setmode(GPIO.BCM)
            gp_out = 4
            GPIO.setup(gp_out, GPIO.OUT)
            servo = GPIO.PWM(gp_out, 50)
            servo.start(0)
            servo.ChangeDutyCycle(10.5)
            time.sleep(0.5)
            servo.stop()
            GPIO.cleanup()
    return False


#clf.connect(rdwr={'on-connect': connected})
#clf.close()

def roop():
    clf = nfc.ContactlessFrontend('usb')
    while roop_flg:
        clf.connect(rdwr={'on-connect': connected})
    clf.close()
    
def start():
    roop_flg = True

def stop():
    roop_flg = False

if __name__ == '__main__':
    start()

