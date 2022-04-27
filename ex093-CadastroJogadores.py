jogador = {}
gols = list()
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range (0, partidas):
    gols.append(int(input(f'Quantos gols na {p+1}ª partida? ')))
for g in gols:
    total += g

jogador['gol'] = gols
jogador['total'] = total
print('-=' *30)
print(jogador)
print('-=' *30)
print(f'Nome do jogador: {jogador["nome"]}.')
print(f'Gols em suas respectivas partidas: {jogador["gol"]}')
print(f'Marcou num total de {jogador["total"]} gols.')
print('-=' *30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p, g in enumerate(gols):
    print(f'  =>Na partida {p+1}, fez {g} gols')
print(f'Num total de {jogador["total"]} gols.')

