#Crie um algoritimo que leia o salario atual de um funcionario
#e mostre o valor atualizado com 15% a mais
sal = float(input('Salário atual do funcionário:\033[32mR$\033[m'))
salnovo = sal + (sal * 15 / 100)
print('Salário atual do funcionário, com {}15%{} de aumento passa a ser:{}R${:.2f}{}'.format('\033[36m', '\033[m', '\033[32m', salnovo, '\033[m'))