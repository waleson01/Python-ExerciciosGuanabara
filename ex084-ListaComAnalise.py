pessoas = list()
dado = list()
qtde = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    qtde += 1


    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar: [S/N] ')).strip().lower()[0]
    if resp != 's':
        break
peso = list()

print(f'Ao todo, você cadastrou {qtde} pessoas.')
for a in range(0, len(pessoas)):
    peso.append(pessoas[a][1])
print(f'O MAIOR peso é de {max(peso):.2f} foi do(a) ', end='')
for b in range(0, len(pessoas)):
    if pessoas[b][1] >= max(peso):
        print(f'{pessoas[b][0]}... ', end='')

print(f'\nO MENOR peso é de {min(peso):.2f} foi do(a) ', end='')
for c in range(0, len(pessoas)):
    if pessoas[c][1] <= min(peso):
        print(f'{pessoas[c][0]}... ', end='')




'''print(f'O maior peso é de {maiorpeso:.2f} do(a) ', end='')
for a in range(0, len(pessoas)):
    if pessoas[a][1] >= maiorpeso:
        maiorpeso = pessoas[a][1]
        print(f'{pessoas[a][0]}, ', end='')
print(f'\nO menor peso é de {menorpeso:.2f} do(a) ', end='')
for b in range(0, len(pessoas)):
    if pessoas[a][1] <= menorpeso:
        menorpeso = pessoas[b][1]
        print(f'{pessoas[b][0]}, ', end='')'''
