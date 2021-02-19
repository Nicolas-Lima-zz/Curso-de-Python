pv = int(input('Digite um valor: '))
sv = int(input('Digite outro: '))
opcao = 1
while opcao != 5:
    print('''Suas opções:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        soma = pv + sv
        print('A soma entre {} e {} é {}'.format(pv, sv, soma))
    elif opcao == 2:
        multiplicacao = pv * sv
        print('A multiplicação de {} e {} é {}'.format(pv, sv, multiplicacao))
    elif opcao == 3:
        if pv > sv:
            print('Maior é o {}'.format(pv))
        elif sv > pv:
            print('Maior é o {}'.format(sv))
    elif opcao == 4:
        pv = int(input('Digite um valor: '))
        sv = int(input('Digite outro: '))
    elif opcao == 5:
        print('FIM DO PROGRAMA')
