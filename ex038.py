n1 = int(input('\033[34mDigite o primeiro numero: '))
n2 = int(input('\033[35mDigite o segundo numero: '))

if n1 > n2:
    print('\033[33mO PRIMEIRO número é o MAIOR!')
elif n1 < n2:
    print('\033[36mO SEGUNDO número é o MAIOR!!')
elif n1 == n2:
    print('\033[1;34;43mNão existe maior, os valores são IGUAIS!!!\033[m')
