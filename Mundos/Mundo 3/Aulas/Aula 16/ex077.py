lista = []
while True:
    palavras = (str(input('Digite a palavra: ')))
    continuar = str(input('Quer adicionar mais palavras? [S/N] ')).upper()[0]
    lista.append(palavras)
    if continuar == 'N':
        break
for palavra in lista:
    print(f'\nNa palavra {palavra} temos', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
