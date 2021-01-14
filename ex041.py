from datetime import date
ano = int(input('Digite o ANO de nascimento do atleta: '))
hoje = date.today()
idade = hoje.year - ano
print('O a atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria MIRIM!!')
elif idade > 9 and idade <= 14:
    print('Categoria  INFANTIL!!')
elif idade > 14 and idade <= 19:
    print('Categoria JUNIOR!!')
elif idade > 19 and idade <= 20:
    print('Categoria SÊNIOR!!')
elif idade > 20:
    print('Categoria MASTER!!')
