# Calcule o valor a ser pago por um produto considerando seu preço normal e condição de pagamento
# á vista dinheiro ou cheque = 10% desconto          - até 2x no cartão = preço normal
# á vista no cartão = 5% desconto                    - 3x ou mais no cartão = 20% juros
print('{:^40}'.format('LOJA DA ROROH'))
preco = float(input('Preço das compras:R$ '))
print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro ou pix
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual a forma escolhida: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f} sem juros.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totpar = int(input('Quantas parcelas: '))
    parcela = total / totpar
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(totpar, parcela))
else:
    total = preco
    print('OPÇÃO INVALIDA, Tente novamente!')
print('Sua compra de {:.2f} vai custar no total R${:.2f}.'.format(preco, total))