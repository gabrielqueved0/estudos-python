valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5 :

    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    escolha = int(input('Qual a sua escolha? '))
    if escolha == 1 :
        soma = valor1 + valor2
        print(f'A soma de {valor1} e {valor2} é {soma}')
    elif escolha == 2 :
        mult = valor1 * valor2
        print(f'A multiplicação de {valor1} e {valor2} é {mult}')
    elif escolha == 3 :
        maior = valor1 if valor1 > valor2 else valor2
        print(f'O número de maior valor é {maior}')
    elif escolha == 4 :
        print('Informe os valores novamente')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif escolha == 5 :
        print('Saindo...')
    else:
        print('Opção invalida!')