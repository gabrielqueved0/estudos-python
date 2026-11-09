agenda = []
clientes = {}
print('-----AGENDAMENTO-----')
for c in range(0, 2):
    clientes['nome'] = str(input('Nome: '))
    clientes['serviço'] = str(input('Qual serviço desejado? '))
    agenda.append(clientes.copy())
for n in agenda:
    print(f' O cliente {n['nome']} marcou horário para {n['serviço']}')
print('-' *20)