from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura' '')
computador = randint(0, 2)
print('''Suas opçôes:
PEDRA
PAPEL
TESOURA''')
jogador = str(input('Sua escolha: ')).upper()
print('JO')
sleep(0.2)
print('KEN')
sleep(0.2)
print('PÔ')

print('O computador escolheu {} e você {}'.format(lista[computador], jogador))
if computador == 0:
    if jogador == 'PEDRA':
        print('{}EMPATE{}'.format('\033[1;33m', '\033[m'))
    elif jogador == 'PAPEL':
        print('{}Você ganhou!{}'.format('\033[1;32m', '\033[m'))
    elif jogador == 'TESOURA':
        print('{}O computador ganhou!{}'.format('\033[1;31m', '\033[m'))
    else:
        print('{}Opção inválida!{}'.format('\033[1;31m', '\033[m'))
elif computador == 1:
    if jogador == 'PAPEL':
        print('{}EMPATE{}'.format('\033[1;33m', '\033[m'))
    elif jogador == 'PEDRA':
        print('{}O computador ganhou!{}'.format('\033[1;31m', '\033[m'))
    elif jogador == 'TESOURA':
        print('{}Você ganhou!{}'.format('\033[1;32m', '\033[m'))
    else:
        print('{}Opção inválida!{}'.format('\033[1;31m', '\033[m'))
elif computador == 2:
    if jogador == 'TESOURA':
        print('{}EMPATE{}'.format('\033[1;33m', '\033[m'))
    elif jogador == 'PEDRA':
        print('{}Você ganhou!{}'.format('\033[1;32m', '\033[m'))
    elif jogador == 'PAPEL':
        print('{}O computador ganhou!{}'.format('\033[1;31m', '\033[m'))
    else:
        print('{}Opção inválida!{}'.format('\033[1;31m', '\033[m'))

