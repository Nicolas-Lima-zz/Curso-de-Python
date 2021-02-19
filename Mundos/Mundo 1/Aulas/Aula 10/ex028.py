from random import randint
escolha = int(input('Escolha um número de 0 a 5: '))
computador = randint(1, 5)
print('O computador escolheu {} e você {}'.format(computador, escolha))
if escolha == computador:
    print('Você venceu!')
else:
    print('Você perdeu!')