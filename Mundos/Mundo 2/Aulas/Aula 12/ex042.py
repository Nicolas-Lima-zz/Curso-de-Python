r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if r1 == r2 == r3:
      print('{}EQUILÁTERO{}'.format('\033[1;32m', '\033[m'))
    elif r1 != r2 != r3 != r1:
        print('{}ESCALENO{}'.format('\033[1;32m', '\033[m'))
    else:
        print('{}ISÓSCELES{}'.format('\033[1;32m', '\033[m'))
else:
  print('Os segmentos acima {}NÃO PODEM FORMAR{} um triângulo'.format('\033[1;31m', '\033[m'))