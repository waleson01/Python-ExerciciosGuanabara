import math
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
h = ((co**2) + (ca**2)) ** (1/2)
print ('Hipotenusa: {:.2f}'.format(h))
print('O valor da Hipotenusa é: {:.2f}'.format(math.hypot(co,ca)))