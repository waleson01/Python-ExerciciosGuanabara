from random import randint
cont = 0

print('-=' * 10)
print('Jogo - PAR OU ÍMPAR')
print('-=' * 10)
while cont <= 3:
    num = int(input('\nDigite um numero: '))
    pc = randint(0, 9)

    par = ' '
    while par not in 'pi':
        par = str(input('Par ou ímpar? [P/I] ')).strip().lower()[0]

    result = num + pc

    if par == 'i':
        if result % 2 == 0:
            print(f'Você escolheu {num} e o Computador escolheu {pc}, o resultado deu {result}. Você PERDEU!')
            break
        else:
            print(f'Você escolheu {num} e o Computador escolheu {pc}, o resultado deu {result}. Você GANHOU!')
            cont += 1

    if par == 'p':
        if result % 2 == 0:
            print(f'Você escolheu {num} e o Computador escolheu {pc}, o resultado deu {result}. Você GANHOU!')
            cont += 1
        else:
            print(f'Você escolheu {num} e o Computador escolheu {pc}, o resultado deu {result}. Você PERDEU!')
            break

print(f'\nO jogo acabou e voce venceu {cont} vezes..')