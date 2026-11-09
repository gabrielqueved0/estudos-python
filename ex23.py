familia = ('Noodle', 'Laura', 'Nedio', 'Cleo',  'Gabriel',)
for n in familia:
    print(f'\nNa palavra {n.upper()} temos ', end= '')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra , end=' ')
    print('de vogais')
