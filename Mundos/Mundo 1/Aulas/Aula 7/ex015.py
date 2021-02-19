qd = float(input('Quantidade de dias alugados: '))
qk = float(input('Quantidade de Km percorridos: '))
r = (qk * 0.15) + (qd * 60)
print('O total a pagar é de R${:.2f}'.format(r))