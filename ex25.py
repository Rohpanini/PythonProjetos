# Crie um programa que leia o nome de alguem e diga se ela tem Silva em seu nome completo
nomcomplet = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva?: {}.'.format('silva' in nomcomplet.lower()))