a = []
while True:
    a.append(int(input('Digite um número: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? (S/N): ')).upper()[0]
    if resp not in 'S':
        break
menor = min(a)
maior = max(a)
print('Fim do programa!')
print(f'A sua lista de valores ficou: {a}')
print(f'O menor valor da lista é {menor}')
print(f'O maior valor da lista é {maior}')
