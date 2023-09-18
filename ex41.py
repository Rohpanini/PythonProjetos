# Leia o ano de nascimento de um atleta e diga em qual categoria ele está
# sendo até 9 anos= mirim
# até 14= infantil
# até 19= junior
# até 20= sênior
# acima = master
from datetime import date
ano = int(input('Qual ano você nasceu: '))
hj = date.today().year
idade = hj-ano
if idade <=9:
    print('Sua categoria é a MIRIM!')
elif idade <=14:
    print('Sua categoria é a INFANTIL!')
elif idade <= 19:
    print('Sua categoria é a JUNIOR!')
elif idade <= 25:
    print('Sua categoria é a SÊNIOR!')
else:
    print('Sua categoria é a MASTER!')

