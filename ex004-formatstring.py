n = input('Digite um ALGO: ')
print('O tipo primitivo desse valor é: {}'.format(type(n)))
print('Só tem espaços? {}'.format(n.isspace()))
print('É um numero? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É Alfanumérico? {}'.format(n.isalnum()))
print('Está em Maiúscula? {}'.format(n.isupper()))
print('Está em Minuscula? {}'.format(n.islower()))
print('Está Capitalizada? {}'.format(n.istitle()))
