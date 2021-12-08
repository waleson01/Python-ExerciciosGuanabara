valores = list()
par = list()
impar = list()
while True:
    num = int(input('Digite um numero: '))
    valores.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    c = ' '
    while c not in 'sn':
        c = str(input('Deseja continuar? S/N ')).strip().lower()[0]
    if c == 'n':
        break
print(f'Lista com todos os numeros digitados: {valores}')
print(f'Lista com todos os numeros pares: {par}')
print(f'Lista com todos os numeros impares: {impar}')

