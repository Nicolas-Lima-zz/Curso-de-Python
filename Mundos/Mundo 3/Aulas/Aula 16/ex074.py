from random import sample
lista = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
lista = sample(lista, 5)
for c in range(0, 5):
    print(lista[c], end=' ')
