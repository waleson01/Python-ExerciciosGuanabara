valores = list()
cont = 0
cinco = ''
while True:
    num = int(input('Digite um numero: '))
    valores.append(num)
    cont += 1

    c = ' '
    while c not in 'sn':
        c = str(input('Deseja continuar? S/N ')).strip().lower()[0]
    if c != 's':
        break
print(f'Quantidade de numeros da lista: {cont}') #len(valores)
print(f'Lista na forma decrescente: {sorted(valores, reverse=True)}')
print(f'O numero 5 foi digitado? {"Sim, ele existe na lista" if 5 in valores else "Não está na lista" }')
#aparecer na tela "bla " if tal in lista else "bla bla "
