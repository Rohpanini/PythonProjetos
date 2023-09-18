# ler uma frase pelo taclado e mostrar quantas vezes a letra 'A'
# se repete, em que posição ela aparece pela primeira vez, e pela ultima.
frase = str(input('Digite um frase: ')).upper().strip()
print('A letra a, aparece {} vezes.'.format(frase.count('A')))
print('A posição da primeira letra a é: ', frase.find('A')+1)
print('A ultima posição da letra a é: ', frase.rfind('A')+1)