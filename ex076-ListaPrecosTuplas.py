lista = ('Lapis', 2.50, 'Borracha', 0.50, 'Caderno', 56.80)

print('-'*40)
print(f'{"Lista de Preços":^40}')
print('-'*40)

for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R$ {lista[c]:.2f}')