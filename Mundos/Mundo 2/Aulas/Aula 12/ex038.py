np = int(input('Digite o primeiro número: '))
ns = int(input('Digite o segundo número: '))
if np > ns:
    print('O primeiro número é o MAIOR'.format('\033[1:32m', '\033[m'))
elif ns > np:
    print('O segundo número é o MAIOR'.format('\033[1:32m', '\033[m'))
else:
    print('Os dois número são iguais')