lar = float(input('Digite a largura da parede: '))
alt =  float(input('Digite a altura da parede: '))
r = lar * alt / 2
print('Para pintar uma parede com uma dimensão de {:.0f}x{:.0f}, você vai precisar de {}L de tinta.'.format(lar,alt,r))