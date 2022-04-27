lista = [[],[],[]]
maior = 0
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
print('')
print('=-'* 15)

somapar = somacol = 0

for x in range(0,9):
    if x % 2 == 0:
        somapar += x
for y in range(0,3):
    somacol += lista[2][y]


for z in range(0,3):
    if maior <= lista[z][1]:
        maior = lista[z][1]

print(f'A soma dos valores pares é de: {somapar}')
print(f'A soma do valores da terceira coluna é: {somacol}')
print(f'O maior valor da segunda linha é: {maior}')
