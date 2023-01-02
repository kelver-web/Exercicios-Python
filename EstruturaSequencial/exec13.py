# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

# A) Para homens: (72.7*h) - 58
# B) Para mulheres: (62.1*h) - 44.7


altura = float(input('Digite a sua altura:  '))
homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7

print(f"Altura ideal para os Homens: {homem:.2f}")
print(f"Altura ideal para as Mulheres: {mulher:.2f}")
