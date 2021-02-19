from random import randint
computador = randint(1, 10)
cont = resultado = 0
while True:
    valor = int(input('Diga um valor: '))
    parouimpar = str(input('Par ou Ímpar? ')).strip().upper()[0]
    while parouimpar != 'P' and parouimpar != 'I':
        parouimpar = str(input('Par ou Ímpar?')).strip().upper()[0]
    soma = valor + computador
    parimpar = soma % 2
    if parimpar == 0:
        resultado = 'PAR'
    if parimpar == 1:
        resultado = 'ÍMPAR'
    print(f'Você jogou {valor} e o computador {computador}. Total de {soma} deu {resultado}')
    if parouimpar == 'I' and parimpar == 0 or parouimpar == 'P' and parimpar == 1:
        break
    if parouimpar == 'I' and parimpar == 1 or parouimpar == 'P' and parimpar == 0:
        cont += 1
        print('''Você venceu
    Vamos jogar novamente!''')
print(f'Você perdeu\nVocê conseguiu vencer {cont} vezes')