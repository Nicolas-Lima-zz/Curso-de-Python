soma = 0
contador = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
     contador = contador + 1
     soma = soma + c
print('A soma de todos os {} números Ímpares múltiplos de 3 entre 1 e 500: {}'.format(contador, soma))
