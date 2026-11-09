numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in ['S', 'N']:
        r = str(input('Resposta inválida! Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print(f'Sua lista ficou: {numeros}')
print(f'Foram digitados {len(numeros)} valores')
numeros.sort(reverse=True)
print(f'Sua lista em ordem decrescente: {numeros}')
if 5 in numeros:
    print('O número 5 está presente na lista!')
else:
    print('O número 5 foi esquecido')