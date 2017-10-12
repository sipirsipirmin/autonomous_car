#!/usr/bin/env python
# -*- coding: utf-8 -*-




import RPi.GPIO as GPIO
import sys
import time
import locale


GPIO.setmode(GPIO.BOARD)

sag_teker = 7
sol_teker = 12

GPIO.setup(sag_teker, GPIO.OUT)
GPIO.setup(sol_teker, GPIO.OUT)

dc = 5

servo_sag = GPIO.PWM(sag_teker,50)
servo_sol = GPIO.PWM(sol_teker,50)

servo_sag.start(1)
servo_sol.start(1)

print('***Connect Battery & Press ENTER to start')
raw_input()

servo_sag.ChangeDutyCycle(5)
servo_sol.ChangeDutyCycle(5)

print('***Press ENTER to start')
raw_input()

while 1:
	try:
		komut = input("komut: ")
	except:
		print "Ooops"
		komut = 2

	if komut == 0:
		break
	elif komut == 1:
		dc = dc + 0.05
		servo.ChangeDutyCycle(dc)
		print("yeni deger: ",dc)
	elif komut == 2:
		dc = dc - 0.05
		servo.ChangeDutyCycle(dc)
		print("yeni değer: ",dc)
	else:
		try:
			dc = float(input("dc gir: "))
		except:
			print "fak yu"
			dc = dc
		servo.ChangeDutyCycle(dc)
		print("yeni değer: ",dc)
#		print(res,dc)

print('***Press ENTER to quit')
raw_input()

GPIO.cleanup()
