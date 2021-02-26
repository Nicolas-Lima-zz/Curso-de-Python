times = 'Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', \
        'Athletico-PR', 'Corinthians', 'Bragantino', 'Ceará SC', 'Atlético-GO', 'Sport Recife', 'Bahia', 'Fortaleza', \
        'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo'
print('=' * 10, 'Os 5 primeiros colocados', '=' * 10, '\n')
for c in range(0, 5):
    print(f'{c + 1}° {times[c]}')
print('')
print('=' * 10, 'Os 4 últimos colocados', '=' * 10)
print('')
for c in range(16, 20):
    print(f'{c + 1}° {times[c]}')
print('')
print('=' * 10, 'Times em ordem alfabética', '=' * 10)
print(f'{sorted(times)}')
print('')
print('=' * 10, 'Posição do time São Paulo', '=' * 10)
print('')
print(f'O time do São Paulo está na {times.index("São Paulo") + 1}° posição')
print('')
print('=' * 51)
