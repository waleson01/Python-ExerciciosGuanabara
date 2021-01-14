print("{:=^40}".format(" Waleson Shop "))
preco = float(input('Digite o valor das compras: '))
print('''Condiçoes de pagamento
    [ 1 ] Dinheiro ou cheque
    [ 2 ] Cartão a vista
    [ 3 ] 2x no Cartão
    [ 4 ] 3x ou mais no Cartão''')

op = int(input('Digite sua opção: '))

if op == 1:
    valor = preco - (preco * 10 / 100 )
    print('O valor total da compra é de \033[34mR${:.2f}\033[m.'.format(valor))
elif op == 2:
    valor = preco - (preco * 5 / 100)
    print('O valor total da compra é de \033[34mR${:.2f}\033[m'.format(valor))
elif op == 3:
    valor = preco
    par = valor / 2
    print("O valor das parcerlas em 2x é de R$ {:.2f}".format(par))
    print('O valor total da compra é de \033[34mR${:.2f}\033[m'.format(valor))
elif op == 4:
    par = int(input("Quantidade de parcelas: "))
    valor = preco + (preco * 20 / 100)
    tpar = valor / par
    print("O valor das parcelas em {}x é de R$ {:.2f}".format(par, tpar))
    print('O Valor total da compra é de \033[34mR$ {:.2f}\033[m'.format(valor))
else:
    print("\033[1;31mOPÇÃO INVÁLIDA!!! Tente novamente.")


