from random import randint
v = 0
while True:
    player = int(input('Digite um valor: '))
    pc = randint(0, 10)
    total = player + pc
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador jogou {pc} e o total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente!')
print(f'GAME OVER! Voce venceu {v} vezes!')
