valor = float(input('Digite o valor do produto: R$'))
print('''Opções de pagamento: 
[ 1 ] Á vista no dinheiro
[ 2 ] Á vista no cartão
[ 3 ] Dividido no cartão''')
opcao = float(input('Condição de pagamento: '))
if opcao == 1:
    print('O valor a ser pago á vista no dinheiro vai ser de R${:.2f}'.format(valor - (10 * valor) / 100))
elif opcao == 2:
    print('O valor a ser pago á vista no cartão vai ser de R${:.2f}'.format(valor - (5 * valor) / 100))
elif opcao == 3:
    cartao = float(input('Digite em quantas vezes: '))
    if cartao <= 2:
     print('O valor a ser pago em {:.0f} vezes no cartão vai ser de R${:.2f}'.format(cartao, valor))
    if cartao >= 3:
     print('O valor a ser pago em {:.0f} vezes no cartão vai ser de R${:.2f}'.format(cartao, valor + (20 * valor) /100))
