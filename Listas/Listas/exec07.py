# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

from math import prod
from functools import reduce


# inteiros = [1, 2, 3, 4, 5]
# soma = sum(inteiros)
# mult = prod(inteiros)
# print(f'Soma: {soma}')
# print(f'Multiplicação: {mult}')


# inteiros = [1, 2, 3, 4, 5]
# soma = reduce(lambda x, y: x + y, inteiros)
# mult = reduce(lambda x, y: x * y, inteiros)
# print(f'Soma: {soma}')
# print(f'Multiplicação: {mult}')
# print(f'Números: {inteiros}')

inteiros = [1, 2, 3, 4, 5]

produto = 1
for numero in inteiros:
    produto *= numero

print(produto)

