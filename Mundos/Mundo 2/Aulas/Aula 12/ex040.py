nu = float(input('Primeira nota: '))
nd = float(input('Segunda nota: '))
media = (nu + nd) /2
if media < 5:
    print('O aluno foi {}REPROVADO{}'.format('\033[1:31m', '\033[m'))
elif media < 7:
    print('O aluno está na {}RECUPERAÇÃO{}'.format('\033[1:33m', '\033[m'))
elif media > 7:
    print('O aluno está {}APROVADO{}'.format('\033[1:32m', '\033[m'))

