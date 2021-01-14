n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Sua media foi de {:.1f}'.format(media))
if media <=5.0:
    print('\nVocê foi REPROVADO!!')
elif media >= 5.1 and media <= 6.9:
    print('\nVocê ficou para RECUPERAÇÃO!!')
elif media >= 7.0:
    print('\nVocê foi APROVADO!!')
