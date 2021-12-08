valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

print(f'O MAIOR valor digitado foi {max(valores)} na posição ', end='')
for i in range(0, 5):
    if valores[i] == max(valores):
        print(i, end='... ')

print(f'\nO MENOR valor digitado foi {min(valores)} na posição ', end='')
for r in range(0, 5):
    if valores[r] == min(valores):
        print(r, end='... ')

