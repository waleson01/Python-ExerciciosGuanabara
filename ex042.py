r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Compriemnto da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('\033[35mDa pra se formar um Triângulo!')
    if r1 == r2 and r1 == r3 :
       # r1 == r2 == r3:
        print('Triangulo \033[34mEquilátero!')
    elif r1 != r2 != r3 != r1:
        print('Triangulo \033[33mEscaleno!')
    else:
        print('Triangulo \033[31mIsóceles!')

else:
    print("\033[36mNão forma um triangulo com esses seguinmento!")
