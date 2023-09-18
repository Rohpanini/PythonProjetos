# Receba um ano e diga se ele é bissexto ou não
from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é \033[1;34mBissexto!\033[m'.format(ano))
else:
    print('O ano de {} \033[1;31mNão\033[m é \033[1;34mBissexto!\033[m'.format(ano))