lista = []
listaPar = []
listaImpar = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
lista.sort()
listaPar.sort()
listaImpar.sort()
print(f'Sua lista total: {lista}')
print(f'A lista de números pares: {listaPar}')
print(f'A lista de números impares: {listaImpar}')