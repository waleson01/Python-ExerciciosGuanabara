sal = float(input('Digite o salario do funcionario: R$'))
if sal >= 1250:
    aumento = (sal * 10) / 100 + sal
    print('O salário com aumento é de R${:.2f}'.format(aumento))
else:
    aumento = (sal * 15) / 100 + sal
    print('O salário com aumento é de R${:.2f}'.format(aumento))
    