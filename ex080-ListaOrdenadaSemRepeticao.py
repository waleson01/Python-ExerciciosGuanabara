lista = list()

'''para adicionar o primeiro numero coloca ele na "ultima" posição usando o lista.append.
  para adicionar numero no meio verifica o valor se eh '''

for c in range(0, 5):
        valor = int(input('Digite um valor: '))
        if c == 0 or valor > lista[-1]: #se ele for o primeiro numero ou o numero foi maior q o ultimo valor da lista add com append no final.
                lista.append(valor)
                print('Adicionado no final da lista...')
        else:
                pos = 0
                while pos < len(lista): #primeiro descobre a posição do numero digitado
                        if valor <= lista[pos]: #verificando em qual posição o numero vai ser inserido
                                lista.insert(pos, valor)
                                print(f'adicionado na posição {pos}')
                                break
                        pos += 1
print('-'*40)
print(f'Valores digitado em ordem: {lista}')
