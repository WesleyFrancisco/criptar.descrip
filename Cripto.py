__author__ = 'wesley'
# -*- coding: utf-8 -*-
#Programa de criptografia de palavras

from encript import criptar
from decript import decriptar

print 'Bem vindo'
while True:
    print 'O que voce gostaria de fazer?'
    fazer = int(raw_input("escolha uma opção:\n 1 Criptografar\n 2 Descriptografar\n 3 Sair\n"))

    if fazer==1:
        while True:
            criptar()
            break

    elif fazer==2:
        while True:
            decriptar()
            break
    else:
        break

print "Obrigado volte sempre!"