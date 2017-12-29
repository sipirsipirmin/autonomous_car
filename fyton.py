#!/usr/bin/env python
#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import sys
from ctypes import *
from time import sleep

GPIO.setmode(GPIO.BOARD)

add = CDLL('./gyro.so')

add.main()

sleep(14)

yaw_zero = add.main(0)

sol_pin_1 = 36
sol_pin_2 = 38
sol_pin_pwm = 40

sag_pin_1 = 11
sag_pin_2 = 15
sag_pin_pwm = 7

tolerans = 10

hiz = 21

def sol(pwm_sol):
	pwm_sol.ChangeDutyCycle(hiz)
	pwm_sag.ChangeDutyCycle(0)
def sag(pwm_sag):
	pwm_sag.ChangeDutyCycle(hiz)
	pwm_sol.ChangeDutyCycle(0)

def init_sol(): # pwm_sag dönderecek
	#---------- sol teker -------------------
	GPIO.setup(sol_pin_1,GPIO.OUT)
	GPIO.setup(sol_pin_2,GPIO.OUT)
	GPIO.setup(sol_pin_pwm,GPIO.OUT) #pwm

	GPIO.output(sol_pin_1,False)
	GPIO.output(sol_pin_2,True)

	pwm_sol = GPIO.PWM(sol_pin_pwm,50)

	pwm_sol.start(0)

	return pwm_sol

def init_sag(): #pwm_sol dönderecek
	#---------- sag teker -------------------
	GPIO.setup(sag_pin_1,GPIO.OUT)
	GPIO.setup(sag_pin_2,GPIO.OUT)
	GPIO.setup(sag_pin_pwm,GPIO.OUT) #pwm

	GPIO.output(sag_pin_1,False)
	GPIO.output(sag_pin_2,True)

	pwm_sag = GPIO.PWM(sag_pin_pwm,50)

	pwm_sag.start(0)

	return pwm_sag

pwm_sol = init_sol()
pwm_sag = init_sag()
GPIO.output(sol_pin_1,False)
GPIO.output(sol_pin_2,True)
GPIO.output(sag_pin_1,False)
GPIO.output(sag_pin_2,True)

print "hazır"
while True:
	yaw = add.main(0)
	if (yaw - yaw_zero) > 0 + tolerans:
		while yaw - yaw_zero > tolerans:
			yaw = add.main(0)
			sag(pwm_sag)
		pwm_sol.ChangeDutyCycle(0)
		pwm_sag.ChangeDutyCycle(0)
		print "sol"
	elif (yaw - yaw_zero) < 0 - tolerans:
		while yaw - yaw_zero < tolerans:
			yaw = add.main(0)
			sol(pwm_sol)
		
		pwm_sol.ChangeDutyCycle(0)
		pwm_sag.ChangeDutyCycle(0)
		print "sag"
	if add.main(0)-yaw_zero < -tolerans and add.main(0)-yaw_zero > tolerans:
		print "sıfırla"
		pwm_sol.ChangeDutyCycle(0)
		pwm_sag.ChangeDutyCycle(0)






