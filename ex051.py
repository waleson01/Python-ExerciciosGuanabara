primeiro = int(input("Digite o Primeiro Termo (PA): "))
razao = int(input("Digite a Razão: "))
decimo = primeiro + (10 - 1) * razao

for r in range(primeiro, decimo + razao, razao):
    print("{} ".format(r), end='-> ')
print("ACABOU!")