# Monte um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor
num = int(input('Digite um numero: '))
print('O sucessor de \033[32m{}\033[m é \033[4;33m{}\033[m, e o antecessor é \033[4;33m{}\033[m! '.format(num, (num+1), (num-1)))