# Aluguel de carros. Escreva um programa que pergunte a quantidade de tempo alugado,
# quantos kms rodados, e mostre o valor a pagar.
alug = float(input('Quantos \033[4;33mdias\033[m alugados: '))
kms = float(input('Quantos \033[4;36mKm\033[m rodados: '))
valalug = alug*60 + kms*0.15
print('O valor a pagar pelo aluguel do carro é de:\033[32mR${:.2f}\033[m'.format(valalug))