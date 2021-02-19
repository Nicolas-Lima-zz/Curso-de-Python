a = int(input('Digite o número da tabuada: '))
for c in range(1, 10):
    print('{} x {:2} = {}{}{}'.format(a, c, '\033[1;32m', a * c, '\033[m'))