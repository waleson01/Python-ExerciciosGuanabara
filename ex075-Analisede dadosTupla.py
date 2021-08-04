lista = ()
nove = par = pos = 0
for c in range(0,4):
    num = int(input('Digite um numero: '))
    lista += (num,)
    if num == 9:
        nove += 1
    if num == 3:
        lista.index(3)
    if num % 2 == 0:
        par += 1

print(f'Numeros da Tupla: {lista}')
print(f'O numero 9 apareceu: {nove} vezes.')
print(f'O primeiro numero 3 apareceu na {pos+1}ª posição.')
print(f'Essa lista tem {par} par(s).')
