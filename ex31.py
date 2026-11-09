from operator import itemgetter
from random import randint
from time import sleep
ranking = list()
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),}
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("="*30)
print("Ranking dos jogadores")
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: O {v[0]} tirou {v[1]}.')
    sleep(1)