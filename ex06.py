# Monte um algoritmo que leia um numero, e mostre na tela seu dobro seu triplo e sua raiz quadrada
num = int(input('Digite um numero: '))
print('\033[35mO dobro deste numero é:\033[m{} \n\033[34mO triplo:\033[m{} \n\033[33mE sua raiz quadrada:\033[m{}!'.format((num*2), (num*3), (num**(1))))
