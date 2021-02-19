pn = int(input('Digite o primeiro número: '))
sn = int(input('Digite o segundo número: '))
tn = int(input('Digite o terceiro número: '))
if pn > sn and pn > tn:
    print('O primeiro número é o maior.'.format(pn))
if pn < sn and pn < tn:
    print('O primeiro número é o menor'.format(pn))
if sn > pn and sn > tn:
    print('O segundo número é o maior'.format(sn))
if sn < pn and sn < tn:
    print('O segundo número é o menor'.format(sn))
if tn > pn and tn > sn:
    print('O terceiro número é o maior'.format(tn))
if tn < pn and tn < sn:
    print('O terceiro número é o menor'.format(tn))
