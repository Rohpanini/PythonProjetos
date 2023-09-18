# Crie um programa  para aprovar um emprestimo de uma casa, lendo o valor da casa o salario do comprador
# e em quantos anos ele pretende pagar, calcule a prestação e veja se o valor execede os 30% do salario
# ou não. Se execeder não sera aprovado.
casa = float(input('Valor da Casa:R$ '))
sal = float(input('Qual o o valor do seu salário:R$ '))
anos = int(input('Em quantos anos pretende pagar: '))
presta = casa/(12*anos)
apagar = sal - 0.30*sal
print('Para pagar uma casa de R${} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, presta))
if presta <= apagar:
    print('Seu emprestimo foi \033[34mAPROVADOR!!!\033[m')
else:
    print('Seu emprestimo foi \033[31mNEGADO!\033[m')