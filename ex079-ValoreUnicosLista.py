valores = list()

while True:
    valor = int(input('Digite um Valor: '))
    if valor in valores:
        print(f'Valor ja existente!!!')
    else:
        valores.append(valor)
        print(f'Adicionado com sucesso!')
    c = ' '
    while c not in 'sn':
        c = str(input('Deseja continuar? S/N ')).strip().lower()[0]
    if c != 's':
        break
print(f'Você digitou os valores: {sorted(valores)}')
