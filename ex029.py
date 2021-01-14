km = int(input('Qual a velocidade atual do carro?  '))
if km > 80:
    multa = (km - 80) * 7
    print('Voce foi MULTADO!')
    print('A multa foi no valor de R${},00'.format(multa))
else:
    print('Velocidade Permitida!')