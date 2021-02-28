tupla = ('Morango', 'Jabuticaba', 'Casa', 'Carro', 'Zebra', 'Tigre', 'Peixe')
codigo = '\n'
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')