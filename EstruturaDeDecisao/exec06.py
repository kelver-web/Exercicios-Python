# Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Digite o 1º número:  '))
n2 = float(input('Digite o 2º número:  '))
n3 = float(input('Digite o 3º número:  '))

if n1 > n2 and n1 > n3:
    print(f"{n1:.0f} é o maior número")
elif n2 > n1 and n2 > n3:
    print(f"{n2:.0f} é o maior número")
else:
    print(f"{n3:.0f} é o maior número")