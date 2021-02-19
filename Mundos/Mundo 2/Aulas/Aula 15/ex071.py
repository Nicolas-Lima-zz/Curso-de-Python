amarelo = '\033[1;33m'
final = '\033[m'
vermelho = '\033[1;31m'
acaba = '\033[m'
print(f'{vermelho}''='f'{acaba}' * 20, f'{amarelo}Banco do Brasil{final}', f'{vermelho}''='f'{acaba}' * 20)
print('')
valor = int(input('Digite o valor a ser sacado: R$'))
total = valor
totalcedulas = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'{totalcedulas} cédulas de {ced} reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalcedulas = 0
        if total == 0:
            break