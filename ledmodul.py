import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


isQrCode = False


def gateOpenGreen():
    #green LED
    ledPinGr = 8
    for i in range(10):
        GPIO.setup(ledPinGr, GPIO.OUT)
        print("Green Led is on!")
        GPIO.output(ledPinGr, GPIO.HIGH)
        time.sleep(2)
        print("Led off!")
        GPIO.output(ledPinGr, GPIO.LOW)
        time.sleep(0.5)

def carNotRecognisedBlau():
    #Blau LED
    ledPinBl = 18
    GPIO.setup(ledPinBl, GPIO.OUT)
    print("Car is not recognised--> Blue is on!")
    GPIO.output(ledPinBl, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(ledPinBl, GPIO.LOW)
    time.sleep(1)
