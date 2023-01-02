# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

# notas = []
#
# for i in range(1, 5):
#     n = int(input(f'Digite a {i}º nota: '))
#     notas.append(n)
#     media = sum(notas) / len(notas)
# print(f'A média do aluno foi: {media}')

# nota1 = int(input(f'Nota 1: '))
# nota2 = int(input(f'Nota 2: '))
# nota3 = int(input(f'Nota 3: '))
# nota4 = int(input(f'Nota 4: '))
#
# media = (nota1+nota2+nota3+nota4) / 4
# print(f'A média do aluno foi: {media}')

# notas = []
# for n in range(1, 5):
#     notas.append(int(input(f'Digite a {n}º nota: ')))
#     media = sum(notas) / len(notas)
# print(media)


notas = [int(input(f'Digite a {i}º nota: ')) for i in range(1, 5)]
media = sum(notas) / len(notas)
print(f'A média do aluno foi {media}')
