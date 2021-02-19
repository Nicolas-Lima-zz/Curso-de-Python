soma = 0
cont = 0
for d in range(0, 6):
    a = int(input('Digite um número inteiro: '))
    if a % 2 == 0:
     soma += soma + a
     cont += cont + 1
print('A soma de todos os {} números é {}'.format(cont, soma))

