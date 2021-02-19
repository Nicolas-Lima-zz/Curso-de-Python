negativo = '-'
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
    for c in range(1, 10):
        print('{} x {} = {}'.format(tabuada, c, tabuada * c))
print('Tabuada encerrada. Volte sempre!')