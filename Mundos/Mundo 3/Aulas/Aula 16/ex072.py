tupla = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
escolher = int(input('Digite um número entre 0 e 20: '))
while escolher > 20:
    escolher = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {tupla[escolher]}')
