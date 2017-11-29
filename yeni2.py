#!/usr/bin/env python
#-*- coding: utf-8 -*-

from init_ve_temel_hareketler import *
import sys
import time
import socket               # Import socket module

GPIO.setmode(GPIO.BOARD)

pwm_sol = init_sol()
pwm_sag = init_sag()

hiz = 0
donus_hizi = 11 
hiz_carpani = 1
while 1:
	gelen =raw_input("kontrol:")
	print gelen
	if gelen == '0':
		temp = gelen
		if hiz > 3:
			ileri()
		hiz = hiz + 1
	elif gelen == '2':
		temp = gelen
		if hiz < 3:
			geri()
		hiz = hiz - 1
	elif gelen == '3':
		pwm_sag.ChangeDutyCycle(abs(hiz) +  donus_hizi)
		continue
	elif gelen == '1':
		pwm_sol.ChangeDutyCycle(abs(hiz) +  donus_hizi)
		continue
	elif gelen == '5':
		hiz = 0
		pwm_sag.ChangeDutyCycle(abs(hiz))
		pwm_sol.ChangeDutyCycle(abs(hiz))
		break
	pwm_sag.ChangeDutyCycle(abs(hiz))
	pwm_sol.ChangeDutyCycle(abs(hiz))
	hiz_carpani = 0
	print "hiz: ", hiz
	time.sleep(0.2)
GPIO.cleanup()
