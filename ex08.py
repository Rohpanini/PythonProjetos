# Crie um programa que leia um valor em metro e mostre na tela os centímetros e os milímetros desse valor
medida = float(input('Digite o valor em métros: '))
cm = medida*100
mm = medida*1000
cor = {'azul': '\033[36m'}
print('A medida de {}m é de:\n{}{:.0f}{}cm e {}{:.0f}{}mm.'.format(medida, cor['azul'], cm, '\033[m', cor['azul'], mm ,'\033[m'))
