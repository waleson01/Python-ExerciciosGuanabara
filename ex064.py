soma = cont = num = 0
print('Somatoria de numero... Para sair digite 999')
while num != 999:
    num = int(input('Digite um numero: '))
    if num != 999:
        soma += num
        cont += 1
print('Foi digitado {} numeros e a soma deles é {}.'.format(cont, soma))