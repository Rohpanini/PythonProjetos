# Crie um programa que leia o nome completo de uma pessoa, e
# Mostre o nome com todas as letras maiúsculas
# Com todas minúsculas
# Quantas letras sem considerar espaços
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é: ', nome.upper())
print('Seu nome em letras maiúsculas é: ', nome.lower())
print('Seu nome completo tem {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
# ou: separa= nome.split
# print('Seu primeiro nome tem {} letras'.format(len(separa[0])))