# Leia um nome completo e diga seu primeiro nome e seu ultimo.
nom = str(input('Digite seu nome completo: ')).strip()
nome = nom.split()
print('Seu primeiro nome é: ', nome[0])
print('Seu ultimo nome é: ', nome[-1])
