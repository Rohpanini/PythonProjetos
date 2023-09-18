# Receba o valor em km de uma viagem, e mostre o preço da passagem
# sendo R$0,50 por km para viagens até 200km
# e R$0,45 por km para viagens acima de 200km
kms = float(input('Qual é a distância da sua viagem?: '))
if kms <= 200:
    preço = kms * 0.50
else:
    preço = kms * 0.45
print('Sua Viagem de {:.0f}km ficara no valor de \033[32mR${:.2f}\033[m.'.format(kms, preço))
print('\033[36mTenha uma ótima viagem ;)\033[m')

#preço = kms * 0.50 if kms <= 200 else kms * 0.45