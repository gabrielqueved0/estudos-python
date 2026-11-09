numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor Duplicado! Erro ao adicionar')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in ['S', 'N']:
        r = str(input('Resposta invalida! Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('='*30)
numeros.sort()
print(f'Sua lista ficou: {numeros}')

