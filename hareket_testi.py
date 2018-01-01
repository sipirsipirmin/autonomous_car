#!/usr/bin/env python
#-*- coding: utf-8 -*-

from init_ve_temel_hareketler import *
import sys
import time
import socket
from temel_hareketler import *

GPIO.setmode(GPIO.BOARD)


with temel_hareketler() as araba:
    while 1:
        try:
            gelen = araba.clientsocket.recv(15)
            if gelen == '':
            	print "null"
            	break

            if gelen == 'yukari': # hız arttır, eğer hız -10 dan büyükse ileri gitmeye başla
                araba.hizlan()

            elif gelen == 'asagi': # hız azalt, eğer hız 10 dan küçükse geri gitmeye başla
            	araba.yavasla()

            elif gelen == 'sol': # sola dön
            	araba.sol()
                continue

            elif gelen == 'sag': # sağa dön
            	araba.sag()
                continue

            elif gelen == 'kapat':
            	break

            elif gelen == 'duzelt':
                araba.duzelt()

            elif gelen == 'r': # hızı 15 e ayarlayacak
                araba.hiz_ata(15)
            else:
            	print "!! : " , gelen

            time.sleep(0.20)
    	except KeyboardInterrupt:
    		break
    	except ValueError: # burada daha düşük bi değere getirsek yeter, çıkmaya gerek yok
    		print "Motor Değeri 100 ü aştı. aman yavaş", hiz, " d_hizi: ", d_hizi
    		break
