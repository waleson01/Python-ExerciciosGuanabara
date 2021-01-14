import math
a = float(input('Digite o angulo: '))
print('O seno do angulo {}° é de: {:.2f}'.format(a, math.sin(math.radians(a))))
print('O conseno do angulo {}° é de: {:.2f}'.format(a, math.cos(math.radians(a))))
print('A tangente do angulo {}° é de: {:.2f}'.format(a, math.tan(math.radians(a))))
