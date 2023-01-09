# Faça um Programa que leia três números e mostre o maior e o menor deles.

'''numeros = []

while len(numeros) < 3:
    numeros.append(float(input('Digite o número: ')))

print(f'Maior Número: {max(numeros):.0f}')
print(f'Menor Número: {min(numeros):.0f}')'''

numeros = [float(input(f"Digite o {x+1}º número:  ")) for x in range(3)]
print(f"Maior Número: {max(numeros):.0f}")
print(f"Menor Número: {min(numeros):.0f}")