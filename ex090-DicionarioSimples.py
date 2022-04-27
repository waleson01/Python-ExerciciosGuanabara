aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
print(f'Nome do Aluno é {aluno["nome"]}')
print(f'A media é igual a {aluno["media"]}')
if aluno['media'] >= 7.0:
    print(f'Situação: Aprovado!')
else:
    print('Situação: Reprovado')
