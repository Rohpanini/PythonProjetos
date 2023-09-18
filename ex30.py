# Ler um numero e dizer se ele é par ou impar
num = int(input('Digite um numero: '))
if num % 2 == 0:
    print('O numero digitado é \033[1;31mPar\033[m!')
else:
    print('O numero digitado é \033[1;36mÍmpar\033[m!')