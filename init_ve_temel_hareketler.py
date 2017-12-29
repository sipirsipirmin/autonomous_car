#!/usr/bin/env python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import sys
import time
import socket

GPIO.setmode(GPIO.BOARD)

class temel_hareketler:
	fiki = 2
	def __init__(self):
		self.sol_p = 5
	def yaz(self):
		print fiki
sol_pin_1 = 36
sol_pin_2 = 38
sol_pin_pwm   = 40

sag_pin_1 =  11
sag_pin_2 = 15
sag_pin_pwm   = 7

def baglanti_kur():
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = 5003
	serversocket.bind(('', port))
	serversocket.listen(5)
	(clientsocket, address) = serversocket.accept()
	return clientsocket

def sol(hiz,pwm_sag,d_hizi):
	try:
		pwm_sag.ChangeDutyCycle(int(abs(hiz) + abs(d_hizi)))
		d_hizi = d_hizi + 5
	except ValueError:
		print "top speed"

def sag(hiz,pwm_sol,d_hizi):
	try:
		pwm_sol.ChangeDutyCycle(int(abs(hiz) + abs(d_hizi)))
		d_hizi = d_hizi + 5
	except ValueError:
		print "top speed"
def cikis(pwm_sag, pwm_sol):
	pwm_sag.ChangeDutyCycle(0)
	pwm_sol.ChangeDutyCycle(0)
	GPIO.cleanup()

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

def ileri():
	GPIO.output(sol_pin_1,False)
	GPIO.output(sol_pin_2,True)

	GPIO.output(sag_pin_1,False)
	GPIO.output(sag_pin_2,True)

def geri():
	GPIO.output(sol_pin_1,True)
	GPIO.output(sol_pin_2,False)

	GPIO.output(sag_pin_1,True)
	GPIO.output(sag_pin_2,False)
