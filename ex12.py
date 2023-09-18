# Faça um algoritimo que leia o valor de um produto e desconte 5% do valor total dele
val = float(input('Valor do produto:\033[32mR$\033[m'))
vald = val-0.05*val
cores = {'verm': '\033[31m',
         'verd': '\033[32m'}
print('O valor do produto com desconto de {}5%{} é {}R${:.2f}{}'.format(cores['verm'], '\033[m', cores['verd'], vald, '\033[m'))