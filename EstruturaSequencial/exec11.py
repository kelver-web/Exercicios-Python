# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.


int1 = int(input('Digite o 1º inteiro:  '))
int2 = int(input('Digite o 2º inteiro:  '))
float1 = float(input('Digite um decimal:  '))

resp1 = (int1 * 2) * (int2 / 2)
resp2 = (int1 * 3) + float1
resp3 = (float1 ** 3)

print(f'O produto do dobro do primeiro com a metade do segundo: {resp1}')
print(f'A soma do triplo do primeiro com o terceiro: {resp2}')
print(f'O terceiro elevado ao cubo: {resp3}')