# Crie um programa que leia um numero real qualquer do teclado, e converta para inteiro.
'''from math import trunc
nmr = float(input('Digite um numero Real: '))
print('O numero {} em sua porção inteira é {}.'.format(nmr, trunc(nmr)))'''

'''from math import floor
nmr = float(input('Digite um numero Real: '))
print('O numero {} em sua porção inteira é {}.'.format(nmr, floor(nmr))'''

nmr = float(input('Digite um Numero Real: '))
print('O numero \033[34m{}\033[m em sua porção inteira é \033[4;30;44m{}\033[m.'.format(nmr, int(nmr)))
