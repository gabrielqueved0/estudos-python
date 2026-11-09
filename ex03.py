nascimento = int(input('Ano de nascimento: '))
idade = 2026 - nascimento
print('Quem nasceu em {} tem {} anos em 2026'.format(nascimento, idade))
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))

elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))