lista = ()
nove = par = pos = 0
for c in range(0, 4):
    num = int(input('Digite um numero: '))
    lista += (num,)
    if num == 9:
        nove += 1
    if num == 3:
        lista.index(num)
    if num % 2 == 0:
        par += 1

print(f'Numeros da Tupla: {lista}')
print(f'O numero 9 apareceu: {nove} vezes.')
print(f'Numero 9: {lista.count(9)} vezes')
print(f'O primeiro numero 3 apareceu na {lista.index(3)+1}ª posição.')
if 3 in lista:
    print(f'Posição do 3: {lista.index(3)+1}ª')
else:
    print('O valor 3 não foi digitado.')
print(f'Essa lista tem {par} numero(s) par(s).')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
