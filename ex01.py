num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print('A conversão do número {} para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print("A conversão do número {} para octal é igual a {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print('A conversão do número {} para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida')