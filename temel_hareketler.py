#!/usr/bin/env python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import sys
import time
import socket

GPIO.setmode(GPIO.BOARD)

class temel_hareketler:
	clientsocket = 	None
	port = 			5003

	sol_pin_1 = 	None
	sol_pin_2 = 	None
	sol_pin_pwm = 	None
	sag_pin_1 = 	None
	sag_pin_2 = 	None
	sag_pin_pwm = 	None

	pwm_sag = 		None
	pwm_sol = 		None

	def __enter__(self):
		self.sol_pin_1 = 36
		self.sol_pin_2 = 38
		self.sol_pin_pwm   = 40

		self.sag_pin_1 =  11
		self.sag_pin_2 = 15
		self.sag_pin_pwm   = 7

		self.baglanti_kur()
		self.init_sag()
		self.init_sol()
		return self
	def __exit__(self, exc_type, exc_value, traceback):
		self.pwm_sag.ChangeDutyCycle(0)
		self.pwm_sol.ChangeDutyCycle(0)
		GPIO.cleanup()
	def hiz(self,hiz): # ikisine de aynı değeri ata
		self.pwm_sag.ChangeDutyCycle(hiz)
		self.pwm_sol.ChangeDutyCycle(hiz)
	
	def baglanti_kur(self):
		print "baglantı bekleniyor"
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		serversocket.bind(('', self.port))
		serversocket.listen(5)
		(self.clientsocket, address) = serversocket.accept()
		print "baglantı geldi"

	def init_sag(self): #pwm_sol dönderecek
		#---------- sag teker -------------------#
		GPIO.setup(self.sag_pin_1,GPIO.OUT)
		GPIO.setup(self.sag_pin_2,GPIO.OUT)
		GPIO.setup(self.sag_pin_pwm,GPIO.OUT) #pwm

		GPIO.output(self.sag_pin_1,False)
		GPIO.output(self.sag_pin_2,True)

		self.pwm_sag = GPIO.PWM(self.sag_pin_pwm,50)

		self.pwm_sag.start(0)


	def init_sol(self): # pwm_sag dönderecek
		#---------- sol teker -------------------
		GPIO.setup(self.sol_pin_1,GPIO.OUT)
		GPIO.setup(self.sol_pin_2,GPIO.OUT)
		GPIO.setup(self.sol_pin_pwm,GPIO.OUT) #pwm

		GPIO.output(self.sol_pin_1,False)
		GPIO.output(self.sol_pin_2,True)

		self.pwm_sol = GPIO.PWM(self.sol_pin_pwm,50)

		self.pwm_sol.start(0)

	def sol(self,hiz,d_hizi):
		try:
			self.pwm_sag.ChangeDutyCycle(int(abs(hiz) + abs(d_hizi)))
		except ValueError:
			print "top speed"

	def sag(self,hiz,d_hizi):
		try:
			self.pwm_sol.ChangeDutyCycle(int(abs(hiz) + abs(d_hizi)))
		except ValueError:
			print "top speed"

	def ileri(self):
		GPIO.output(self.sol_pin_1,False)
		GPIO.output(self.sol_pin_2,True)

		GPIO.output(self.sag_pin_1,False)
		GPIO.output(self.sag_pin_2,True)

	def geri(self):
		GPIO.output(self.sol_pin_1,True)
		GPIO.output(self.sol_pin_2,False)

		GPIO.output(self.sag_pin_1,True)
		GPIO.output(self.sag_pin_2,False)
