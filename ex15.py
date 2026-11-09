from random import randint
computador = randint(0, 10)
print('Fala Noob, pensei em um número aleatorio entre 0 e 10.')
print('Duvido acertar, tenta ai.')
acerto = False
tentativas = 0
while not acerto:
    jogador = int(input('Qual seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acerto  = True
    else:
        if jogador < computador:
            print('Mais... tente novamente: ')
        elif jogador > computador:
            print('Menos... tente novamente: ')
print(f'Acertou mizeravi... com {tentativas} tentativas.')