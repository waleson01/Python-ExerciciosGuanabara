import random, playsound
from time import sleep
num = int(input('Digite um numero de 0 - 5: '))
print('PROCESSANDO...')
sleep(2)
#pc = random.randrange(5)+1
pc = random.randint(0, 5)
if pc == num:
    print('O computador pensou no numero {} e voçê no numero {}, Voçê venceu!'.format(pc, num))
    playsound.playsound('certa-resposta.mp3')
else:
    print('O computador pensou no numero {} e voçê no numero {}, Voçê perdeu!'.format(pc, num))
    playsound.playsound('errou.mp3')


