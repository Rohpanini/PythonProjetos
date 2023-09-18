#Escreva um programa que receba a temperatura em C e converta para F
temp = float(input('Informe a temperatura em Grau Celsius: '))
f = (temp * 9 / 5) + 32
print('A temperatura de \033[32m{}\033[m Graus Celsius corresponde a \033[31m{}\033[m Graus Fahrenheit'.format(temp, f))