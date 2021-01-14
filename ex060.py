num = int(input('Digite um numero: '))
cont = num
resultado = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    resultado *= cont
    cont -= 1
print('{}'.format(resultado))
print('O fatorial de {} é = {}'.format(num, resultado))
