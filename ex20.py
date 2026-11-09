totalMaior = totalMasc = totalMulher =  0
while True:
     print('-' *30)
     print('CADASTRE UMA PESSOA!!')
     idade = int(input('Idade: '))
     sexo = ' '
     while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).upper()[0]
     if idade >= 18:
         totalMaior += 1
     if sexo == 'M':
         totalMasc += 1
     if sexo == 'F' and idade < 20:
         totalMulher += 1
     resp = ' '
     while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
     if resp == 'N':
         break
print(f'O total de pessoas cadastradas com mais de 18 anos foram: {totalMaior}')
print(f'Foram cadastrados {totalMasc} homens.')
print(f'Foram cadastradas {totalMulher} mulheres com menos de 20 anos.')
