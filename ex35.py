# Leia o tamanho de três retas e diga se elas podem ou não formar um triangulo.
print(10*'\033[33m-+-\033[m')
print('\033[30;43mVamos Analizar Triângulo...\033[m')
print(10*'\033[30m-+-\033[m')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mAs retas acima Podem formar um triângulo!\033[m')
else:
    print('\033[31mAs retas acima Não Podem formar um triângulo!\033[m')
