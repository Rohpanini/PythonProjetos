# Escreva um programa que leia o ano que a pessoa nasceu e diga se esta na hora,
# se vai chegar ou se ja passou da hora dele se alistar, e tambem diga quanto falta ou quanto se atrasou.
from datetime import date
ano = int(input('Qual ano você nasceu: '))
hoje = date.today().year
idade = hoje - ano
if idade == 18:
    print('Está na hora de se alistar.')
elif idade < 18:
    saldo = 18 - idade
    anos = hoje + saldo
    print(f'Ainda não está na hora de se alistar, faltam {saldo} anos.')
    print(f'Seu alistamento será em {anos}')
else:
    saldo = idade - 18
    anos = hoje - saldo
    print(f'Já passou do tempo de se alistar, faz {saldo} anos.')
    print(f'Seu alistamento foi em {anos}')