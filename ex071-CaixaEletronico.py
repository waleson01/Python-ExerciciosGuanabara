saque = int(input('Qual o valor do saque: '))
total = saque
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0: #escrever comente se o total de cedulas for mairo que 0
            print(f'Total de {totced} cedulas de R$ {ced}')
            
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        totced = 0 #Zerando o contador da celular atual.

        if total == 0:
            break
print('\nFim de operção - Volte sempre!')