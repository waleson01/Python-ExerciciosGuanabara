numero = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
         'onze','doze','treze', 'quatorze', 'quize', 'dezesseis','dezesete','dezoito','dezenove','vinte')

num = int(input('Digite um numero entre 0 e 20: '))
while True:
    if num >= 0 and num <= 20:
        print(f'Parabéns!! Você digitou o número \033[32m{numero[num]}')
        break
    num = int(input(' Numero Invalido!\nDigite um numero entre 0 e 20: '))


