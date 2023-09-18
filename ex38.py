# Leia dois numeros inteiros compare-os e mostre na tela qual valor é maior ou se são iguais.
print('\033[35mDigite dois números, e lhe direi qual deles é o Maior!\033[m')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O Primeiro Número é o Maior!')
elif n2 > n1:
    print('O Segundo Número é o Maior!')
else:
    print('Nenhum, os dois números digitados são iguais!')