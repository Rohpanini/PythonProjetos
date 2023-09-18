# Leia duas notas de um aluno e diga se ele esta retido, aprovado ou ficou de recuperação.
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua Média foi', media)
if media < 5.0:
    print('Você está \033[31mREPROVADO!\033[m')
elif media >= 7.0:
    print('Você foi \033[36mAPROVADO\033[m, meus parabéns.')
else:
    print('Você ficou de \033[33mRECUPERAÇÃO\033[m, estude mais!')