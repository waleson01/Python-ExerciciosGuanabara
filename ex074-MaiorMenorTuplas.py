import random
lista = ()
num = random.randrange(0,100)
maior = num
menor = num
lista += (num,)
for c in range(0, 4):
    num = random.randrange(0,100)
    lista += (num,)
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'Numeros da lista: {lista}')
print(f'Numero maior: {maior}')
print(f'Numero Menor: {menor}')

print(f'Maior numero: {max(lista)}')
print(f'Menor numero {min(lista)}')

