times = ('Flamengo','Palmeiras','Grêmio','Internacional','Athletico-PR','Santos','Corinthians','São Paulo','Atlético-MG','Cruzeiro','Bahia',
        'Fluminense','Botafogo','Ceará','Chapecoense','Vasco da Gama','América','Fortaleza','Atlético-GO','Sport')

print(f'Lista de Times do Brasileirão: {times}')
print(f'Os 5 Primeiros são: {times[0:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª Posição.')
