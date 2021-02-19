altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura ** 2)
print('O seu IMC é de {}{:.1f}{}'.format('\033[1;35m', imc, '\033[m'))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO')
elif imc > 18.5 and imc < 25:
    print('Você está com o  PESO IDEAL')
elif imc > 25 and imc < 30:
    print('Você está com SOBREPESO')
elif imc > 30 and imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')