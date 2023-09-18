# Pergunte o valor do salário de um funcionário e calcule o valor do aumento dele.
# Para salários acima de R$1250,00, aumento de 10%
# Para igual ou menor, aumento de 15%.
slr = float(input('Qual é o valor do seu salário atual?:\033[32mR$\033[m '))
if slr <= 1250:
    novo = slr + 0.15 * slr
else:
    novo = slr + 0.10 * slr
print('O Funcionário que ganhava \033[31mR${:.2f}\033[m, com aumento passa a ganhar \033[30;42mR${:.2f}\033[m.'.format(slr, novo))