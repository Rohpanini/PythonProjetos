# Escreva um programa que faça o computador "pensar" em um numero entre 0 a 5 e peça para
# o usuário tentar descobrir em que numero o computador pensou, e diga se o usuario acertou ou não.
from random import randint
from time import sleep
computador = randint(0, 5)
print(20*'\033[34m-*-\033[m')
print('\033[35mVou Pensar em um Número de 0 a 5, Tente adivinhar...\033[m')
print(20*'\033[34m-*-\033[m')
jogador = int(input('Em que Número eu Pensei?: '))
print('\033[34mProcessando...\033[m')
sleep(3)
print('\033[35mSeu Palpite foi {}, e o numero pensado foi {}\033[m'.format(jogador, computador))
if computador == jogador:
    print('\033[4;32mParabés você ganhou!\033[m')
else:
    print('\033[4;31mO computador venceu!\033[m')
