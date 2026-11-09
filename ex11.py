from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'O total de pessoas maior de idade é {maior}')
print(f'O total de pessoas menor de idade é {menor}')
