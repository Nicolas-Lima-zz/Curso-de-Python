from datetime import date
nascimento = int(input('Digite a data de nascimento: '))
idade = date.today().year - nascimento
if idade < 18:
    print('Faltam {} anos para você se alistar'.format(18 - idade))
elif idade == 18:
    print('Está na hora de você se alistar')
elif idade > 18:
    print('Já se passaram {} anos. Se aliste imediatamente!'.format(idade - 18))


