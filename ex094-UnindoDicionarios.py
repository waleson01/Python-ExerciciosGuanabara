grupo = []
pessoas = dict()

pessoas['nome'] = str(input('Nome: '))
pessoas['sexo'] = str(input('Sexo: '))
pessoas['idade'] = int(input('Idade: '))
print(pessoas)
grupo.append(pessoas['nome'], pessoas['sexo'], pessoas['idade'])

print(grupo)