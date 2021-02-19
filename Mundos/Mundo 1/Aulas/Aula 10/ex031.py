dv = int(input('Distância da viagem em km: '))
if dv <= 200:
    print('A sua viagem custará R${:.2f}'.format(dv * 0.50))
else:
    print('A sua viagem custará R${:.2f}'.format(dv * 0.45))