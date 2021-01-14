from datetime import datetime
maior = 0
menor = 0
for r in range(0, 7):
    nasc = int(input("Digite o ano de nascimento: "))
    now = datetime.now()
    ano = now.year - nasc
    if ano >=21:
        maior = maior + 1
    else:
        menor = menor + 1
print("{} pessoas ATINGIRAM a maior idade e {} NÃO ATINGIRAM a maior idade".format(maior, menor))
