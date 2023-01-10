# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite um número:  "))
num2 = int(input("Digite um número:  "))
num3 = int(input("Digite um número:  "))

if num1 < num3: # 1 3 4 
    num1, num3 = num3, num1 # 4 3 1
elif num1 < num2: # 4 3 1
    num1, num2 = num2, num1 # 4 3 1 
elif num2 < num3:
    num2, num3 = num3, num2

print(f'A ordem decrescente é {num1}, {num2} e {num3}')