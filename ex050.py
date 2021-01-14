lista = []
soma = cont = 0
for r in range(0, 6):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        lista.append(n)
        soma += n
        cont += 1
print(lista)
print("A soma de {} numeros pares informado é de: {} ".format(cont, soma))
