from datetime import date
data = int(input('Digite o ano de nascimento do Jovem: '))
hoje = date.today().year     #definindo variavel data de hoje!
ano = hoje - data
print('Você tem {} anos !'.format(ano))
if ano < 18:
    rest = 18 - ano
    print('Você ainda não atingiu a idade para se alistar! Faltam {} anos pra vc se aliastar!'.format(rest))
    saldo = hoje + rest
    print('Sem alistamento será em {}'.format(saldo))
elif ano == 18:
    print('Hora de se alistar  IMEDIATAMENTE!')
elif ano > 18:
    rest = ano - 18
    print('Já passou {} anos do tempo de se alistar.'.format(rest))
    saldo = hoje - rest
    print('Deveria ter se alistado no ano de {}.'.format(saldo))
