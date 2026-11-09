from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' OPÇÕES DE JOGADAS:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Escolha sua jogada:  '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-' * 30)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-' * 30)
if computador == jogador:
    print('EMPATE')
elif computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
    print('O computador vence')

else:
    print('O jogador vence')
