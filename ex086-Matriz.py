lista = [[],[],[]]
for i in range(0, 3):
    valor = int(input(f'Digite um valor para [{0}, {i}]: '))
    lista[i].append(valor)

for p in range(0, 3):
    valor = int(input(f'Digite um valor para [{1}, {p}]: '))
    lista[p].append(valor)

for c in range(0, 3):
    valor = int(input(f'Digite um valor para [{2}, {c}]: '))
    lista[c].append(valor)

print('=-'* 15)
for a in range(0,3):
    print(f'[ {lista[a][0]} ]', end='')
print('')
for s in range(0,3):
    print(f'[ {lista[s][1]} ]', end='')
print('')
for d in range(0, 3):
    print(f'[ {lista[d][2]} ]', end='')


matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' *30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}', end='')
    print()