tupla = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze' \
    , 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    escolher = int(input('Digite um número entre 0 e 20: '))
    while escolher > 20 or escolher <= -1:
        escolher = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {tupla[escolher]}')
    continuar = str(input('Quer continuar: [S/N] ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N] '))
    if continuar == 'N':
        break
