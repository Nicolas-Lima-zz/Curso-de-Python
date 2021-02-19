sa = float(input('Salário atual do funcionário: R$'))
sf = sa + (sa * 15 / 100)
print('Um funcionário que recebia R${:.2f} vai passar a receber R${:.2f}'.format(sa,sf))