# Leia a velocidade de um carro, se ultrapassar 80km escrever uma mensagem de 'você foi multado'
# custando R$7,00 por cada km acima de 80.
km = int(input('Qual velocidade a sua velocidade atual?: '))
mul = (km - 80) * 7
if km > 80:
    print('\033[1;31mMULTADO!\033[m')
    print('Você exedeu o limite de 80km/h e sera multado no valor de \033[31mR${:.2f}\033[m'.format(mul))
print('\033[4;33mTenha um Bom Dia! Dirija com segurança!\033[m')