numero = int(input('Digite um número: '))
print('''Escolha em qual das bases converter:
( 1 ) Para binário
( 2 ) Para octal
( 3 ) Para hexadecimal''')
opc = int(input('Escolha sua opção: '))
if opc == 1:
    print('O número {}{}{} convertido para binário é {}{}{}'.format('\033[0:32m', numero, '\033[m', '\033[0:31m', bin(numero)[2:], '\033[m'))

elif opc == 2:
    print('O número {}{}{} convertido para octal é {}{}{}'.format('\033[0:32m', numero, '\033[m', '\033[0:31m', oct(numero)[2:], '\033[m'))

else:
    print('O número {}{}{} convertido para hexadecimal é {}{}{}'.format('\033[0:32m', numero, '\033[m', '\033[0:31m', hex(numero)[2:], '\033[m'))