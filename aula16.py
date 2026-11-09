num = ('zero', 'um', 'dois', 'três', 'quatro','cinco', 'seis', 'sete','oito', 'nove', 'dez')
sn = ' '
while True:
    escolha = int(input('Digite um valor entre 0 e 10: '))
    if 0 <= escolha <= 10:
        print(f'O valor que você digitou foi {num[escolha]}')
    else:
        print('Tente novamente, digite um valor entre 0 e 10: ')
        continue
    sn = str(input('Quer continuar? (S/N): 0')).upper()[0]
    if sn not in 'S':
        break