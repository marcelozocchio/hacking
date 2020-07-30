# -*- coding: CP1252 -*-

import hashlib

def quebra():

    a = input("Digite o hash MD5: ")
    b = input("Digite o dicionário: ")

    linelist = [line.rstrip('\n') for line in open(b)]
    for i in linelist:
        c = i.encode('latin1')
        c1 = hashlib.md5(c).hexdigest()
        if c1 == a:
            print(i)
            break
        else:
            pass
    print("Final da busca")

quebra()
