num = 1
while num > 0:
    cont = 1
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 30)
    while cont <= 10:
        if num < 0:
            break
        print(f'{num} X {cont} = {num*cont}')
        cont += 1
    print('=' * 30)
print('\nPrograma tabuada encerrado. Volte Sempre!')