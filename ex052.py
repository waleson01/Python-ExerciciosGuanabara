total = 0
n = int(input("Digite um numero inteiro: "))
for c in range(1, n+1):
  if n % c == 0:
    print('\033[34m', end='')
    total += 1
  else:
    print('\033[32m', end='')

  print('{} '.format(c), end='')

print("\n\033[mO numero {} foi divisivel {} vezes".format(n, total))

if total == 2:
  print("Numero Primo")
else:
  print("Não é um numero primo!")
