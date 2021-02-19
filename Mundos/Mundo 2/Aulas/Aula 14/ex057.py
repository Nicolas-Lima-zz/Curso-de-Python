sexo = str(input('Digite o seu sexo: ')).upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Opção inválida. Tente novamente! ')).upper()
if sexo == 'F':
 print('Sexo {} registrado com sucesso!'.format(sexo.replace('F', 'FEMININO')))
else:
    print('Sexo {} registrado com sucesso!'.format(sexo.replace('M', 'MASCULINO')))






