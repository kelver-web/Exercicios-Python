# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.


# numeros = [int(input(f'Dite o {i}º número: ')) for i in range(1, 21)]
# par = [i for i in numeros if i % 2 == 0]
# impar = [i for i in numeros if i % 2 == 1]
# print(par)
# print(impar)

# numeros = [int(input(f'Dite o {i}º número: ')) for i in range(1, 6)]
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# impares = list(filter(lambda x: x % 2 == 1, numeros))
# print(f'Pares: {pares}')
# print(f'Impares: {impares}')

pares = []
impares = []
for i in range(1, 10):
    numero = int(input(f'Digite o {i}º número: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Pares: {pares}')
print(f'Impares: {impares}')
