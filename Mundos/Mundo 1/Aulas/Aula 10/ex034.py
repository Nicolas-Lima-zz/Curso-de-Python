sal = float(input('Digite o salário do funcionário: R$'))
if sal <= 1250:
    print('O novo salário do funcionário com um aumento de 15% será R${:.2f}'.format(sal + (15 * sal / 100)))
else:
    print('O novo salário do funcionário com um aumento de 10% será R${:.2f}'.format(sal + (10 * sal / 100)))