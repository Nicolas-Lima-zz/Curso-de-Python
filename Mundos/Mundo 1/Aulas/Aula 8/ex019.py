from random import choice
au = str(input('Primeiro aluno: '))
ad = str(input('Segundo aluno: '))
at = str(input('Terceiro aluno: '))
aq = str(input('Quarto aluno: '))
la = au,ad,at,aq
le = choice(la)
print('O aluno escolhido foi: {}'.format(le))