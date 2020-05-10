#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
 
import serial #importacao do modulo serial
ser = serial.Serial('COM3') #abre porta serial COM*
while True:
   leitura = ser.readline() #le caracteres recebidos
   if leitura >= "100":
            print "alta luminosidade no local"       
   else:
            print "luminosidade muito baixa"   
ser.close()