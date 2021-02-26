from random import sample
lista = tuple(sample(range(10), 5))
print('Os 5 números sorteados:\n')
simbolo = '-'
for c in range(0, 5):
    if c == 4:
        simbolo = '\n'
    print(lista[c], end=f' {simbolo} ')
print(f'\nO menor número sorteado: {min(lista)}\nO maior número sorteado: {max(lista)}')
