somapreco = maiscaro = conta = 0
menorproduto = ''
print('-' * 30)
print('{: ^30}'.format('Mercado Barato'))
print('-' * 30)
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço: '))
    conta += 1
    somapreco += preco

    if somapreco >= 1000:
        maiscaro += 1
    if conta == 1 or preco < menorpreco:
        menorpreco = preco
        menorproduto = produto

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print('-' * 20)
    if cont == 'N':
        print('{:-^40}'.format('Fim do Programa'))
        break

print(f'A soma de todos os produtos: R${somapreco:2.2f}')
print(f'Total de produtos mais caros que R$1000: {maiscaro:2}')
print(f'O produto mais barato foi {menorproduto} e seu valor é de R${menorpreco:2.2F}.')