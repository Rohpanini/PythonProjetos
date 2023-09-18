# Crie um progama que leia um numero qualquer entre 0 e 9999, e mostre na tela cada um de seus digitos
numero = int(input('Digite um numero entre 0 e 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('\033[32munidades\033[m:', u)
print('\033[36mdezenas\033[m:', d)
print('\033[35mcentenas\033[m:', c)
print('\033[33mmilhares\033[m:', m)