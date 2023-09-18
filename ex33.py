# Leia 3 numeros e diga qual é o maior e qual é o menor
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O \033[4;33mMaior\033[m Número é:', maior)
print('O \033[4;36mMenor\033[m Número é:', menor)