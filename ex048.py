print("Soma de numero impares entre 1 - 500")
soma = cont = 0
for r in range(1, 500, 2):
        if r % 3 == 0:
            cont += 1
            soma += r
print("A soma de {} numero impares entre 1 e 500 é de {}".format(cont, soma))
