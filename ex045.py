import random, time
print('Vamos ver ser você consegue vencer do computador numa partida de Jokenpô!!')
op = str(input('Pedra, Papel ou Tesoura? \nDigite sua opção:  ')).strip().lower()
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)



print('\n\033[1;31mJO', end=''), time.sleep(0.6)
print('\033[1;33mKEN', end=''), time.sleep(0.6)
print('\033[1;36mPÔ\033[m\n'), time.sleep(0.2)

if op == 'pedra' and pc == 'tesoura':
    print('Você escolheu \033[34m{}\033[m e o Computador escolheu \033[32m {} \033[m. Você venceu!!'.format(op, pc))
elif op == 'pedra' and pc == 'papel':
    print('Você escolheu \033[34m{}\033[m e o Computador escolheu \033[32m {} \033[m. Você perdeu!!'.format(op, pc))
elif op == 'tesoura' and pc == 'pedra':
    print('Você escolheu \033[34m{}\033[m e o Computador escolheu \033[32m {} \033[m. Você perdeu!'.format(op, pc))
elif op == 'tesoura' and pc == 'papel':
    print('Você escolheu \033[34m{}\033[m e o Computador escolheu \033[32m {} \033[m. Você venceu!!'.format(op, pc))
elif op == 'papel' and pc == 'pedra':
    print('Você escolheu \033[34m{}\033[m e o Computador escolheu \033[32m {} \033[m . Você venceu!!'.format(op, pc))
elif op == 'papel' and pc == 'tesoura':
    print('Você escolheu \033[34m{}\033[m e o Computador escolheu \033[32m{} \033[m. Você perdeu!!'.format(op, pc))
elif op == pc:
    print('Você escolheu \033[34m{}\033[m e o Computador escolheu \033[32m{} \033[m. EMPATOU!!'.format(op, pc))
else:
    print('Opção invalida! Por favor escolha PAPEL, PEDRA OU TESOURA')
