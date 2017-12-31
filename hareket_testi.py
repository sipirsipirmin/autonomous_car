#!/usr/bin/env python
#-*- coding: utf-8 -*-

from init_ve_temel_hareketler import *
import sys
import time
import socket               # Import socket module
from temel_hareketler import *

GPIO.setmode(GPIO.BOARD)


artis_miktari=2
hiz = 10
d_hizi = 5

with temel_hareketler() as araba:
    while 1:
        try:
            gelen = araba.clientsocket.recv(15)
            if gelen == '':
            	print "null"
            	break

            if gelen == 'yukari': # hız arttır, eğer hız -10 dan büyükse ileri gitmeye başla
            	if hiz > -10:
            		ileri()
            		if hiz < 0:  # -10,+10 aralığında motorlar bir reaksiyon göstermediği için bu aralığı atlıyoz
            			hiz = 10 # -10,+10 aralığında motorlar bir reaksiyon göstermediği için bu aralığı atlıyoz
            	hiz = hiz + artis_miktari
                print hiz

            elif gelen == 'asagi': # hız azalt, eğer hız 10 dan küçükse geri gitmeye başla
            	if hiz < 10:
            		geri()
            		if hiz > 0:    # -10,+10 aralığında motorlar bir reaksiyon göstermediği için bu aralığı atlıyoz
            			hiz = -10 # -10,+10 aralığında motorlar bir reaksiyon göstermediği için bu aralığı atlıyoz
            	hiz = hiz - artis_miktari

            elif gelen == 'sol': # sola dön
            	araba.sol(hiz,d_hizi)
            	d_hizi = d_hizi + 5
            	#hiz = hiz + artis_miktari

            	print "sol motor hızı: " , d_hizi + hiz
            	print "sag motor hızı: " , hiz
            	continue

            elif gelen == 'sag': # sağa dön
            	araba.sag(hiz,d_hizi)
            	d_hizi = d_hizi + 5
            	#hiz = hiz + artis_miktari

            	print "sag motor hızı: " , d_hizi + hiz
            	print "sol motor hızı: " , hiz
            	continue

            elif gelen == 'kapat':
            	break

            elif gelen == 'duzelt':
            	d_hizi = 5

            elif gelen == 'r': # hızı 15 e ayarlayacak
            	hiz = 12
            	d_hizi = 5
            else:
            	print "!! : " , gelen
            	continue
            	#break
    		d_hizi = 5
            araba.hiz(abs(hiz))

            print "hiz: ", hiz
            time.sleep(0.20)
    	except KeyboardInterrupt:
    		break
    	except ValueError: # burada daha düşük bi değere getirsek yeter, çıkmaya gerek yok
    		print "Motor Değeri 100 ü aştı. aman yavaş", hiz, " d_hizi: ", d_hizi
    		break
