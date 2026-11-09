from time import sleep
num = [[], []]
valor = 0
print('='*25)
print('INSPECIONANDO VALORES')
for c in range (1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('FIM DA INSPEÇÃO')
print('='*25)
print('Analisando...')
sleep(2)
print('PRONTO!!')
sleep(1)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')