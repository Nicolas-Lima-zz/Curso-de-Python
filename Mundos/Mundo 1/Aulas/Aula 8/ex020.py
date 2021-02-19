from random import shuffle
au = input('Primeiro aluno:')
ad = input('Segundo aluno: ')
at = input('Terceiro Aluno: ')
aq = input('Quarto aluno: ')
la = [au,ad,at,aq]
shuffle(la)
print('A ordem será: {}'.format(la))
