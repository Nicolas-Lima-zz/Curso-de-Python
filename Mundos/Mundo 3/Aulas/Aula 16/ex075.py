lista = []
par = []
num = cont = merda = a = 0
for c in range(0, 4):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par.append(num)
        cont += 1
    if num == num:
        num = num
    lista.append(num)
print(f'Você digitou os valores {tuple(lista)}')
print(f'O número 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    a = f'O número 3 apareceu na {lista.index(3) + 1}° posição'
else:
    a = 'O número 3 não foi digitado'
print(a)# se o 3 foi digitado ou não
print('Números pares:', end=' ')
for c in range(0, cont):
    print(f'{par[c]}', end=' ')
