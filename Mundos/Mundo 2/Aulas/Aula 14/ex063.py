print('-' * 44)
print(' ' * 10, 'Sequência de Fibonacci', ' ' * 10)
print('-' * 44)
quantos = int(input('Quantos termos você quer mostrar? '))
pri = 0
seg = 1
cont = 3
t3 = 0
print('{} → {} '.format(pri, seg), end='')
while cont <= quantos:
    t3 = pri + seg
    print('→ {} '.format(t3), end='')
    pri = seg
    seg = t3
    cont += 1
print('→ FIM')