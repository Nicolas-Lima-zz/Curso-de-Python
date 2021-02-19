num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m ', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('O número {} foi divisível apenas por 1 e por ele mesmo, e por isso ele é um número primo!'.format(num))
else:
    print('E por isso ele não é primo')