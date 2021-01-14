print('-' * 20)
print('CADASTRO DE PESSOAS')

cidade = chomem = cmulher = 0

while True:
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
         cidade += 1
    if sexo == 'M':
        chomem += 1
    if sexo == 'F' and idade < 20:
        cmulher += 1

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if cont != 'S':
        break
print('Relatorio das pessoas cadastradas:')
print(f'Pessoas maiores que 18 anos: {cidade} pessoas.')
print(f'Quantidade de Homens: {chomem} pessoas.')
print(f'Quantidade de Mulheres com mais de 18 anos: {cmulher} pessoas.')
