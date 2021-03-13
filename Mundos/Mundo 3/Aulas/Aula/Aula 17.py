# lista = list(range(0, 10))
# print(lista)
a = ['abacate', 0, 10, 11, 2, 4]
a.append(10)
a.pop(2)
if 5 in a:
    a.remove(2)
else:
    print('Não existe')
a.insert(2, 21)
print(a)
for c, v in enumerate(a):
    print(f'Na posição {c} eu encontrei o valor {v}')
print('Final')
a1 = [1, 2, 3, 4, 10]
b = a1[:]
b[2] = 21
print(a1, b)
for c, i in enumerate(a):
    print(c, i)