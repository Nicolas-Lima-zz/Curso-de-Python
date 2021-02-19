num = int(input('Digite um número para mostrar o seu fatorial: '))
fat = num
f = 1
while fat > 0:
    print('{}'.format(fat), end='')
    print(' x ' if fat > 1 else ' = ', end='')
    f *= fat
    fat -= 1
print('{}'.format(f))