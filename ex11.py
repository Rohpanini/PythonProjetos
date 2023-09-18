#Faça um programa que leia a largura e a altura de uma parede e calcule
#quantos litros de tinta precisara para pintar a area, sanbendo que um litro
#pinta 2m quadrados.
al = float(input('Altura: '))
la = float(input('Largura: '))
ar = al*la
li = ar/2
print('Sua parede de dimenção {} x {} tem a área de {}m.'
      '\nPara pintar sua parede sera necessario {}l de tinta!'.format(al, la, ar, li))

