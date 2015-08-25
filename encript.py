__author__ = 'wesley'
#!-*- conding: utf8 -*-
def criptar():
    while True:
        Palavra = str(raw_input("Digite 3 para sair. Criptografar:"))
        Palavra = Palavra.lower()
        if Palavra=="3":
            print '\n'
            break
            criptar()
        elif len(Palavra) > 0:
            Palavra=Palavra.replace('a', 'z')
            Palavra=Palavra.replace('b', '2')
            Palavra=Palavra.replace('c', '5')
            Palavra=Palavra.replace('d', '6')
            Palavra=Palavra.replace('e', '8')
            Palavra=Palavra.replace('f', '3')
            Palavra=Palavra.replace('g', '4')
            Palavra=Palavra.replace('h', '7')
            Palavra=Palavra.replace('i', '9')
            Palavra=Palavra.replace('j', '!')
            Palavra=Palavra.replace('k', '@')
            Palavra=Palavra.replace('l', '#')
            Palavra=Palavra.replace('m', '$')
            Palavra=Palavra.replace('n', '&')
            Palavra=Palavra.replace('o', '%')

            print '\n', Palavra
        else:
            print "digite apenas letras!!"