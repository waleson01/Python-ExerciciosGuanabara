nome = str(input('Digite um nome: '))

print('Tudo em maiúsculo:  {} '.format(nome.upper()))
print('Tudo em minúsculo:  {} '.format(nome.lower()))
qtd = nome.lower()
qtd = nome.replace(' ', '')
print('Quantidades de letras no total: {}'.format(len(qtd)-nome.count(' ')))
spc = nome.split()
print('O primeiro nome tem:  {} '.format(len(spc[0])))
