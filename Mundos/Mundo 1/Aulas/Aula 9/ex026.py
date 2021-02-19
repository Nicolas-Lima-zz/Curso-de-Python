a = str(input('Escreva uma frase: ')).strip().upper()
print('A letra A apareceu {} vezes!'.format(a.count('A')))
print('Primeira posição que a letra A aparece {}'.format(a.find('A')+1))
print('Última posição que a letra A aparece: {}'.format(a.rfind('A')+1))