n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
soma = n1+n2
cores = {'vermelho': '\033[31m',
         'veb': '\033[1;0;41m',
         'limpa': '\033[m'}
print('A soma de {}{}{} e {}{}{} é igual a {}{}{}'.format(cores['vermelho'], n1, cores['limpa'], cores['vermelho'], n2, cores['limpa'], cores['veb'], soma, cores['limpa']))
