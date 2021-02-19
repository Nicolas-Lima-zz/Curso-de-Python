num = s = cont = media = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    s += num
    cont += 1
media = s / cont
# print('A soma foi', s)
print(f'A média entre os {cont} números foi {media:.2f}')