import RPi.GPIO as GPIO
import time

def start():
    GPIO.setmode(GPIO.BCM)

    gp_out = 4
    GPIO.setup(gp_out, GPIO.OUT)


    servo = GPIO.PWM(gp_out, 50)


    servo.start(0)
    #time.sleep(1)


    servo.ChangeDutyCycle(10.5)
    time.sleep(0.5)
    
    servo.stop()
    GPIO.cleanup()

if __name__=='__main__':
    start()
