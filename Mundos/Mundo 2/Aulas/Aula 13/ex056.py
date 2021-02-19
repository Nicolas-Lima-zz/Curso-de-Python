mulheres = 0
somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = 0
for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(c))
    nome = str(input('Nome: ')).title().strip()
    sexo = str(input('Sexo: [F/M]: ')).title().upper().strip()
    idade = int(input('Idade: '))
    somaidade += idade
    if c == 1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    elif sexo == 'F' and idade < 20:
        mulheres += 1
mediaidade = somaidade / 4
print(
    'A média da idade dessas 4 pessoas é de {}\nO homem mais velho tem {} anos e o nome dele é {}\n{} Mulheres tem menos de 20 anos'.format(
        mediaidade, maioridade, nomevelho, mulheres))
