velocidade = int(input('Digite a velocidade do carro: '))
a = (velocidade - 80)
if velocidade > 80:
    print('Você foi multado em R${:.2f}'.format((velocidade - 80) * 7))
else:
    print('Tenha um bom dia! Dirija com segurança!')