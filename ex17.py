# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo, e calcule e mostre comprimento da hipotenusa.
from math import hypot
co  = float(input('Comprimento do \033[1;33mCateto Oposto\033[m: '))
ca= float(input('Comprimento do \033[1;33mCateto Adjacente\033[m: '))
hi = hypot(co, ca)
print('A \033[4;35mHipotenusa\033[m mede {:.2f}.'.format(hi))

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (ca**2 + co**2) ** (1/2) 
print('A hipotenusa mede {}.'.format(hi))'''

