casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Quantas anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('A prestação para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(', fica o total de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Parabéns, seu emprestimo foi aprovado!')
else:
    print('Empréstimo Negado!!')
