total = totMil = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Qual o produto? '))
    preço = float(input('Qual o valor? R$'))
    total += preço
    cont += 1
    if preço > 1000:
        totMil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
print('Fim do programa!')
print(f'Total da compra foi de R$ {total:.2f}')
print(f'Tivemos {totMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')

