lista = []
num = 0
for c in range(0, 4):
    num = int(input('Digite um número: '))
    lista.append(num)
    tuple(lista)
print(f'O número 9 apareceu {lista.count(9)} vezes')
print(lista)