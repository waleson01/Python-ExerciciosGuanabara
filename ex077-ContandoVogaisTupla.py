lista = 'Bola', 'Caderno'
for c in range(0, len(lista)):
    print(f'\nNa palavra \033[1;33m{lista[c].upper()} \033[0m Tem as vogais: ', end='')
    for vogal in (lista[c]):
       if vogal.lower() in 'aeiou':
           print(vogal, end=' ')
print('')
for p in lista:
    print(f'\n{p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
