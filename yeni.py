#!/usr/bin/env python
#-*- coding: utf-8 -*-

from init_ve_temel_hareketler import *
import sys
import time
import socket               # Import socket module

GPIO.setmode(GPIO.BOARD)

pwm_sol = init_sol()
pwm_sag = init_sag()

clientsocket = baglanti_kur()
artis_miktari=2
hiz = 10
d_hizi = 5

while 1:
	try:
		gelen = clientsocket.recv(15)

		#print "gelen komut:", gelen
		if gelen == '':
			print "null"
			cikis(pwm_sag,pwm_sol)
			sys.exit(1)

		if gelen == 'yukari': # hız arttır, eğer hız -10 dan büyükse ileri gitmeye başla
			temp = gelen
			if hiz > -10:
				ileri()
				if hiz < 0:  # -10,+10 aralığında motorlar bir reaksiyon göstermediği için bu aralığı atlıyoz
					hiz = 10 # -10,+10 aralığında motorlar bir reaksiyon göstermediği için bu aralığı atlıyoz
			hiz = hiz + artis_miktari

		elif gelen == 'asagi': # hız azalt, eğer hız 10 dan küçükse geri gitmeye başla
			temp = gelen
			if hiz < 10:
				geri()
				if hiz > 0:    # -10,+10 aralığında motorlar bir reaksiyon göstermediği için bu aralığı atlıyoz
					hiz = -10 # -10,+10 aralığında motorlar bir reaksiyon göstermediği için bu aralığı atlıyoz
			hiz = hiz - artis_miktari

		elif gelen == 'sol': # sola dön
			sol(hiz,pwm_sag,d_hizi)
			d_hizi = d_hizi + 5
			#hiz = hiz + artis_miktari

			print "sol motor hızı: " , d_hizi + hiz
			print "sag motor hızı: " , hiz
			continue

		elif gelen == 'sag': # sağa dön
			sag(hiz,pwm_sol,d_hizi)
			d_hizi = d_hizi + 5
			#hiz = hiz + artis_miktari

			print "sag motor hızı: " , d_hizi + hiz
			print "sol motor hızı: " , hiz
			continue

		elif gelen == 'kapat':
			cikis(pwm_sag, pwm_sol)
			sys.exit(0)

		elif gelen == 'duzelt':
			d_hizi = 5
			pwm_sag.ChangeDutyCycle(abs(hiz))
			pwm_sol.ChangeDutyCycle(abs(hiz))

		elif gelen == 'r': # hızı 15 e ayarlayacak
			hiz = 12
			d_hizi = 5
		else:
			print "!! : " , gelen
			continue
			#break
		d_hizi = 5
		pwm_sag.ChangeDutyCycle(abs(hiz))
		pwm_sol.ChangeDutyCycle(abs(hiz))

		print "hiz: ", hiz
		time.sleep(0.20)
	except KeyboardInterrupt:
		print "Hemende ctrl c yapmış . Aceleci herif"
		cikis(pwm_sag, pwm_sol)
		sys.exit(1)
	except ValueError:
		print "Motor Değeri 100 ü aştı. aman yavaş", hiz, " d_hizi: ", d_hizi
		cikis(pwm_sag, pwm_sol)
		sys.exit(1)
