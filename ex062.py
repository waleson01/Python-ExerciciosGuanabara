primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = 0
cont = 0
result = primeiro

while cont != 10:
    cont += 1
    print(result, end=' . ')
    result += razao
print('')


termo = -1
while termo != 0:
    termo = int(input('\nDeseja ver mais termos? (Caso não digite 0 para sair)  '))
    cont = 0
   #result = 0
    result = primeiro
    while cont < (10 + termo):
        cont += 1
        print(result, end=' . ')
        result += razao
print('\nFim do Programa!')