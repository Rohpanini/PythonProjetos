# Crie um programa que leia o valor em reais de uma pessoa e mostre na tela quanto em dolar ela tem considerando 3,27$UE=1,00R$
real = float(input('Valor que você tem na carteira:R$ '))
dolar = real/4.88
print('com o valor de \033[1;33mR$\033[m{:.2f} voce pode comprar \033[1;34mUS$\033[m{:.2f}'.format(real, dolar))