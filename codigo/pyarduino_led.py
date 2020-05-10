#!/usr/bin/env/python
# -*- coding: cp1252 -*-

import serial
import time
conexao = serial.Serial('COM3', 9600) # Configuração da conexão

def pisca(tempo=1):
    while True:
        valor = input("digite o valor 1 ==> ligado, 2 ==> desligado, 3 ==> sair: ")
        if valor == 1:
            conexao.write('1') # Escreve 1 no arduino (LED acende)
            print "ligado"
            time.sleep(tempo) # Aguarda n segundos
        elif valor == 2:
            conexao.write('2') # Escreve 2 no arduino (LED apaga)
            print "desligado"
            time.sleep(tempo) # Aguarda n segundos
        else:
            exit();
if __name__ == '__main__': # Executa a função
    pisca()