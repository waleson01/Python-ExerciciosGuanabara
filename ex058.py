import playsound
from random import randint
import time

humano = tentativas = 0
humano = int(input("Digite um numero de 0 - 10: "))
pc = randint(0, 10)
tentativas += 1
print(pc)
while humano != pc:
    print('\033[32mProcessando....\033[m')
    time.sleep(1)
    if humano == pc:
        print("O COMPUTADOR escolheu {} e vc escolheu {}. Você ACERTOU!!".format(pc, humano))
        playsound.playsound('certa-resposta.mp3')
        tentativas += 1
    else:
        if humano < pc:
            print("Você ERROU! Está mais pra cima!")
            humano = int(input('Ente outro numero: '))
            tentativas += 1
        else:
            print("Você ERROU! Está mais pra baixo!")
            humano = int(input('Ente outro numero: '))
            tentativas += 1
print("Você VENCEU o jogo depois de {} tentativas.".format(tentativas))
playsound.playsound('certa-resposta.mp3')
