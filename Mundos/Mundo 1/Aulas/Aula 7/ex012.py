pro = float(input('Preço do produto: R$'))
des = pro - (pro * 5 / 100)
print('O produto que custava {:.2f} vai custar {:.2f}'.format(pro,des))