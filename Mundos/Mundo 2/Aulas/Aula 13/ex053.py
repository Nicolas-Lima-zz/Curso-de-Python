frase = input('Digite uma frase: ').upper().replace(" ", "").strip()
inverso = frase[::-1]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == frase:
    print('Temos um palíndromo!')
else:
    print('A frase digitado não é um palindromo!')