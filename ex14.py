sexo = str(input('Digite seu sexo: [F/M]: ')).upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, digite novamente seu sexo: ')).upper()
print(f'Sexo {sexo} registrado com sucesso!')