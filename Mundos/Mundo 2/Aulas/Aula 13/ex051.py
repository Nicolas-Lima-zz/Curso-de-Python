soma = 0
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
an = pt + (10 - 1) * razao
for c in range(pt, an + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Acabou')
