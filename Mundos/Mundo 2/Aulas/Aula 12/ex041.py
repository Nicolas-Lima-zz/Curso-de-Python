from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: {}MIRIM{}'.format('\033[1;32m', '\033[m'))

elif idade <= 14:
    print('Classificação: {}INFANTIL{}'.format('\033[1;32m', '\033[m'))

elif idade <= 19:
    print('Classificação: {}JUNIOR{}'.format('\033[1;32m', '\033[m'))

elif idade <= 25:
    print('Classificação: {}SÊNIOR{}'.format('\033[1;32m', '\033[m'))
else:
    print('Classificação: {}MASTER{}'.format('\033[1;32m', '\033[m'))