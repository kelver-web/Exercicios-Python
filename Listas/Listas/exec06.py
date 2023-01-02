# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
# num vetor a média de cada aluno, imprima o número de alunos com média maior
# ou igual a 7.0.


medias = []
media_7 = 0

for i in range(1, 3):
    print(f'\nNotas do {i}º aluno')

    media = 0
    for j in range(1, 5):
        media += float(input(f"{j}º nota: "))

    media /= 4
    medias.append(media)
    if media >= 7:
        media_7 += 1

print(f"\nAluno(s) com média maior ou igual a 7 ---> {media_7}.")
