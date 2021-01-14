dias = int(input('Quantidade de dias o carro foi usado: '))
km = float(input('Quantidade de Quilometros percorrido: '))
pdias = dias * 60
tkm = km * 0.15
valor = pdias + tkm
print('Valor total do aluguel do carro é de: R$ {:.2f}'.format(valor))
