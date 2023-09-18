# Crie um programa que leia o nome de uma cidade e diga se ela começa com SANTO
cidade = str(input('Qual o nome da sua cidade?: ')).strip()
print(cidade[:5].upper() == 'SANTO')
