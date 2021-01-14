import time
op = 0
v1 = int(input("Digite o 1° valor: "))
v2 = int(input("Digite o 2° valor: "))

while op != 5:
    print('''       === MENU ===
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')

    op = int(input("\nDigite sua opção: "))

    if op == 1:
        resultado = v1 + v2
        print('O resultado da soma de {} + {} é = {}\n'.format(v1, v2, resultado))

    if op == 2:
        resultado = v1 * v2
        print('O resultado da Multiplicação de {} * {} é = {}\n'.format(v1, v2, resultado))

    if op == 3:
        if v1 == v2:
            print('Os dois valores são iguais!\n')
        if v1 > v2:
            print('O maior valor é {}\n'.format(v1))
        elif v1 < v2:
            print('O maior valor é {}\n'.format(v2))

    if op == 4:
        print('Por favor digite novos numeros..\n')
        v1 = int(input("Digite o 1° valor: "))
        v2 = int(input("Digite o 2° valor: "))

    if op > 5:
        print('Opção invalida! Tente novamente...')

print('Saindo...\n')
time.sleep(2)
print('\033[31mObrigado! Volte sempre!!')