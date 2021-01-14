casa = float(input('\033[33mDigite o Valor da casa: '))
salario = float(input('\033[34mDigite o Salario: '))
anos = int(input('\033[35mQuantidade de anos que vai pagar: '))

meses = anos * 12
porcent = (salario * 30)/100
total = casa / meses

print('\n\033[mTotal em meses: {}'.format(int(meses)))
print('30%  do salario: {:.2f}'.format(porcent))
print('Valor da prestação: {:.2f}'.format(total))
if total < porcent:
    print('\n\033[36mO Emprestimo será \033[30;44mAPROVADO!\033[m')
else:
    print('\n\033[36mO Emprestimo foi \033[30;44mNEGADO!\033[m')
