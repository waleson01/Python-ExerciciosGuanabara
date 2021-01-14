lista = []

for r in range (0, 5):
    peso = float(input("Digite o peso da {}° pessoa: ".format(r+1)))
    lista.append(peso)
print("O maior peso lido foi {}kg".format(max(lista)))
print("O menor peso lido foi {}kg".format(min(lista)))


if r == 1:
    maior = peso
    menor = peso
else:
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso


