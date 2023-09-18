# Crie um algoritmo que leia duas notas de um aluno e depois mostre sua média final
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
med = (nota1+nota2)/2
print('A média final entre {} e {} é igual a: {}{:.1f}{}'.format(nota1, nota2,'\033[36m', med, '\033[m'))