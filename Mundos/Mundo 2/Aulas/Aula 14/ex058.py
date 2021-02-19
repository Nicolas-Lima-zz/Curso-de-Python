from random import randint
computador = randint(0, 10)
cont = 1
jogador = int(input('Tente adivinhar!! [ 0 até 10 ]: '))
while not jogador == computador:
    cont += 1
    if jogador > computador:
        jogador = int(input('Menos... Tente novamente: '))
    elif jogador < computador:
        jogador = int(input('Mais... Tente novamente: '))
print('Você acertou!! O computador jogou {} e você {}.. E você tentou por {} vezes!'.format(computador, jogador, cont))
