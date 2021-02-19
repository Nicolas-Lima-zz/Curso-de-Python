soma = mil = nome = cont = menor = 0
while True:
    print('=' * 30)
    produto = str(input('Nome do produto: ')).title().strip()
    preco = float(input('Preço: R$'))
    soma += preco
    cont += 1
    print('=' * 30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if preco > 1000:
        mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        nome = produto
    if continuar == 'N':
        break
print('=' * 54)
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custou R${menor:.2f}')
print('=' * 54)
