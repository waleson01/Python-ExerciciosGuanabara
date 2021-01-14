import time
print("\033[1:34mContagem Regressiva para o início do estouro dos fogos de artifício!!")
for r in range(10, -1, -1):
    print("\033[33m",r)
    time.sleep(1)
print("\033[1:31mBooooom!")