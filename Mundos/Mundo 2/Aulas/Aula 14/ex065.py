soma = media = maior = menor = cont = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Você quer continuar? [S/N] ')).strip().upper()
media = soma / cont
print('Você digitou {} números e a média entre eles foi {:.2f}'.format(cont, media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
