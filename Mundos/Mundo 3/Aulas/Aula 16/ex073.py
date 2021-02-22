tupla = 'Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', \
        'Athletico-PR', 'Corinthians', 'Bragantino', 'Ceará SC', 'Atlético-GO', 'Sport Recife', 'Bahia', 'Fortaleza', \
        'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo '
print('-=' * 20)
print(f'\nOs cinco primeiros colocados são: {tupla[:5]}\n')
print('-=' * 20)
print(f'\nOs últimos 4 colocados da tabela {tupla[16:]}\n')
print('-=' * 20)
print(f'\nLista dos times em ordem alfabética: {sorted(tupla)}\n')
print('-=' * 20)
print('\nO São Paulo está na {}° posição\n'.format(tupla.index('São Paulo') + 1))
print('-=' * 20)
