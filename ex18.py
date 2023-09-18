# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, casseno e tangente
# desse ângulo
import math
ang = float(input('Qual valor do \033[1;33mangulo\033[m?: '))
coc = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O \033[1;33mângulo\033[m de {} tem o \033[34mCosseno\033[m de {:.2f}'.format(ang, coc))
print('O \033[1;33mângulo\033[m de {} tem o \033[34mSeno\033[m de {:.2f}'.format(ang, sen))
print('O \033[1;33mângulo\033[m de {} tem a \033[34mTangente\033[m de {:.2f}'.format(ang, tan))