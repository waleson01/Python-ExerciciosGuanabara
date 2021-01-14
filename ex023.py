num = int(input('Digite um numero: '))
un = num % 10
print('Unidade: {}'.format(un))
num = (num - un)/10
dez = num % 10
dez = int(dez)
print('Dezenas: {}'.format(dez))
num = (num - dez)/10
cen = num % 10
cen = int(cen)
print('Centenas: {}'.format(cen))
num = (num - cen)/10
mil = num % 10
mil = int(mil)
print('Milhar: {}'.format(mil))

#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10