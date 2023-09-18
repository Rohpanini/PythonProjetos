# Ler o peso e a altura de uma pessoa e calcular o IMC e dier o status de seu peso.
print("\033[35mVamos Calcular o seu IMC.\033[m")
altura = float(input('Digite sua Altura: '))
peso = float(input('Digite seu Peso (kg):'))
imc = peso / (altura**2)
print('Seu IMC é de {:.1f}.'.format(imc))
if 18.5 <= imc < 25:
    print('\033[34mPeso ideal! Parabés.\033[m')
elif 25 <= imc < 30:
    print('\033[32mVocê está com Sobrepeso!\033[m')
elif 30 <= imc < 40:
    print('\033[31mVocê está com Obesidade!\033[m')
elif imc >= 40:
    print('\033[30mVocê estáa com Obesidade Morbida!!!\033[m')
else:
    print('Você está Abaixo do peso.')

