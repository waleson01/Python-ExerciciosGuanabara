lnome = []
lidade = []
lsexo = []
menor = 0
velho = 0
nomevelho = ''
for r in range(0, 5):
    nome = str(input("Digite o nome da {}° pessoa: ".format(r+1))).strip()
    lnome.append(nome)
    idade = int(input("Digite a idade da {}° pessoa: ".format(r+1)))
    lidade.append(idade)
    sexo = str(input("Digite o sexo da {}° pessoa: ".format(r+1))).strip().lower()
    lsexo.append(sexo)

    if sexo == 'feminino' and idade < 20:
        menor =+ 1
    if r == 1 and sexo == 'masculino':
        velho = idade
        nomevelho = nome.upper()
    if sexo == 'masculino' and idade > velho:
        velho = idade
        nomevelho = nome.upper()

print("A media de idade desse grupo é de {:.0f} anos".format(sum(lidade)/len(lidade)))
print("Exitem {} mulheres com menos de 20 anos!".format(menor))
print("O nome do mais velho é {} e ele tem {} anos.".format(nome, velho))
