num = int(input('Digite um numero: '))
print('''Você deseja convertê-lo em: 
    1 - Binário 
    2 - Octal 
    3 - Hexadecimal ''')
op = int(input('Opção desejada: '))

if op == 1:
    print('O numero {} convertido para BINÁRIO é igual a: {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O numero {} convertido para OCTAL é igual a: {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} convertido em HEXADECIMAL é igual a: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
