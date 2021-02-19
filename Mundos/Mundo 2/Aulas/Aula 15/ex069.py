dezoito = homens = mulher = cont = 0
while True:
    print('=' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).upper().strip()
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo [M/F] ')).upper().strip()
    print('=' * 20)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if idade > 18:
        dezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if continuar == 'N':
        break
print('=' * 32)
print(f'{dezoito} pessoas tem mais de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{mulher} mulheres tem menos de 20 anos')
print('=' * 32)