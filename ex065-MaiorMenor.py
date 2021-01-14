cont = media = soma = maior = 0
num = int(input('Digite um numero: '))
maior = num
menor = num
media = num
cont += 1
cc = str(input('Deseja continuar? S - Sim / N - Não  ')).upper().strip()[0]
while cc not in 'N':
    num = int(input('Digite um numero: '))
    cont += 1
    soma += num
    media = soma / cont
    if num > maior:
        maior = num
    if maior < menor:
        menor = num

    cc = str(input('Deseja continuar? S - Sim / N - Não  ')).upper()


print('\nA MEDIA entre os nuúmeros digitados é de {:.2f}.'.format(media))
print('O MAIOR número digitado foi {}.'.format(maior))
print('O MENOR número digitado foi {}.'.format(menor))
