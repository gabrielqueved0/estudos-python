import moedas
num = float(input("Digite um valor: "))
print(f'O dobro de {num} é {moedas.dobro(num)}')
print(f'A metade de {num} é {moedas.metade(num)}')
taxa = int(input('Digite a taxa (%): '))
print(f'Aumentando {taxa}% do valor {num} fica: {moedas.aumentar(num, taxa)}')
print(f'Diminuindo {taxa}% do valor {num} fica: {moedas.diminuir(num, taxa)}')