casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
anos = float(input('Digite em quantos anos ele vai pagar: '))
reso = casa / (anos * 12)
sala = salario * 30 / 100
if reso <= sala:
    print('O empréstimo foi {}APROVADO{} A prestação será de {}R${}{}'.format('\033[1:32m', '\033[m', '\033[0:32m', '\033[m', reso))
else:
    print('O empréstimo foi {}NEGADO{}'.format('\033[1:31m', '\033[m'))
