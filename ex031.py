km = int(input('Digite a distancia da viagem: '))
if km <= 200:
    valor = km * 0.50
    print('O valor total da viagem é de R${:.2f}.'.format(valor))
else:
    valor = km * 0.45
    print('O valor total da viagem é de R${:.2f}.'.format(valor))
