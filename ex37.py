# Escreva um programa wue leia um número inteiro e peça pro usuário escolher qual será a base de conversão
# 1 para binário
# 2 para octal
# 3 para hexadecimal
num = int(input('Digite um número inteiro: '))
print('''Escolha um número para fazer a conversão
[1] para Binário
[2] para Octal
[3] para Hexadecimal''')
opcao = int(input('Sua Oção: '))
if opcao == 1:
    print('{} convertido para Binário é igual a {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Essa opção é invalida! Tente novamente.')