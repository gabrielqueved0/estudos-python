n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
media = (n1 + n2 +n3) / 3
if media >= 7:
    print('Com média {:.1f}, o aluno foi APROVADO!'.format(media))
elif media < 7:
    print('Com média {:.1f}, o aluno foi REPROVADO!'.format(media))