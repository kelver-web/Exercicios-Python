# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite um número:  "))
num2 = int(input("Digite outro:  "))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
else:
    print(f'{num2} é maior que {num1}')