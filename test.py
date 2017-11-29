import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

asd = GPIO.PWM(4,1000)
asd.start(0)

sayac = 10
while sayac < 200:
	asd.ChangeDutyCycle(sayac)
	sleep(2)
	sayac = sayac + 10

asd.stop()
GPIO.cleanup()
