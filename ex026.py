frase = str(input('Digite uma frase: ')).strip().lower()
print('Aparece a letra a {} vezes'.format(frase.count('a')))
print('Primeiro aparece na posição {}.'.format(frase.find('a')+1))
print('Por ultimo na posição {}.'.format(frase.rfind('a')+1))
