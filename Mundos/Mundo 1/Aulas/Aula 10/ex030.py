numero = int(input('Me diga um número qualquer: '))
res = numero % 2
if res == 0:
    print('O número {} é um número PAR'.format(numero))
else:
    print('O número {} é um número ÍMPAR'.format(numero))