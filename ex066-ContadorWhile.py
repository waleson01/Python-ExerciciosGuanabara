cont = soma = 0
while True:
    n = int(input('Digite o numero: (999 para sair) '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foi digitado {cont} e o resultado da soma entre eles é de {soma}.')
