__author__ = 'wesley'
#!-*- conding: utf8 -*-
def decriptar():
    while True:
        Palavra = str(raw_input("Digite 3 para sair. Descriptografar:"))
        Palavra = Palavra.lower()
        if Palavra=="3":
            print'\n'
            break
            criptar()
        elif len(Palavra) > 0:
            Palavra=Palavra.replace('z', 'a')
            Palavra=Palavra.replace('2', 'b')
            Palavra=Palavra.replace('5', 'c')
            Palavra=Palavra.replace('6', 'd')
            Palavra=Palavra.replace('8', 'e')
            Palavra=Palavra.replace('3', 'f')
            Palavra=Palavra.replace('4', 'g')
            Palavra=Palavra.replace('7', 'h')
            Palavra=Palavra.replace('9', 'i')
            Palavra=Palavra.replace('!', 'j')
            Palavra=Palavra.replace('@', 'k')
            Palavra=Palavra.replace('#', 'l')
            Palavra=Palavra.replace('$', 'm')
            Palavra=Palavra.replace('&', 'n')
            Palavra=Palavra.replace('%', 'o')

            print "\n", Palavra
        else:
            print "digite algo por favor!"