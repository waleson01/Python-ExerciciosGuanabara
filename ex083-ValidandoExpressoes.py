exp = str(input('Digite sua expressão: '))
lista = []
ab = fe = 0
for c in exp:
    print(c)
    if '(' == c:
        ab += 1
    elif ')' == c:
        fe += 1
if ab == fe:
    print('expressão correta')
else:
    print('expressão incorreta')

'''
exp = str(input('Digite sua expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('expressão correta')
else:
    print('expressão incorreta')               
'''