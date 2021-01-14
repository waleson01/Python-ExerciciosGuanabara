primeiro = int(input('Digite o Primeiro Termo (PA): '))
razao = int(input('Digite a Razão: '))
cont = 0
resultado = primeiro
while cont != 10:
    cont += 1
    print(resultado, end=' - ')
    resultado += razao
print('Acabou!')