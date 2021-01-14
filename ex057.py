sexo = str(input("Digite seu sexo (M/F): ")).lower()[0].strip()
while sexo not in 'mf':
   sexo = str(input("Sexo Invalido! \nDigite seu sexo (M/F): ")).lower()[0].strip()
print('Sexo valido!')