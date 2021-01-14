r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Compriemnto da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('CONSEGUE formar um triangulo com esses seguimentos!!')
else:
    print('NÃO CONSEGUE formar um triangulo com esses seguimentos !!')
