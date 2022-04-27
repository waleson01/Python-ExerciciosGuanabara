aluno = list()

while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = nota1 + nota2 / 2
    aluno.append([nome, [nota1, nota2], media])

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if cont != 'S':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    opc = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(aluno)-1:
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
