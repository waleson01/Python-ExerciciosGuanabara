numeros = list()

for i in range(0, 7):
    valor = int(input(f'Digite o {i+1}° numero: '))
    numeros.append(valor)

print(f'Numeros PARES digitados são: ', end='')
for p in numeros:
    if p % 2 == 0:
        print(f'{numeros[p]}.', end='')

print(f'\nNumeros IMPARES digitados são: ', end='')
for c in numeros:
    if c % 2 != 0 or numeros == 1:
        print(f'{numeros[c]}.', end='')


