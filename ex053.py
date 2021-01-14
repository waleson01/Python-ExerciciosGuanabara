palavra = str(input("Digite uma frase: ")).strip().upper()
palavra = palavra.replace(" ", "")
inverso = ''

for lista in range(len(palavra) - 1, -1, -1):
    inverso += palavra[lista]
print('Você digitou {} e seu inverso é {}'.format(palavra, inverso))

if inverso == palavra:
    print("Portanto esta frase é um PALÍNDROMO!")
else:
    print("Portanto esta frase NÃO é um PALÍNDROMO")


