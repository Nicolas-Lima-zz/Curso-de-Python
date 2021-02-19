from datetime import date
maiores = 0
menores = 0
for c in range(1, 8):
    a = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    o = date.today().year - a
    if o > 21:
        menores = menores + 1
    else:
        maiores = maiores + 1
print('Das 7 pessoas pessoas digitadas, {} são maiores de idade e {} são menores de idade'.format(maiores, menores))
