# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.
import math

num1 = float(input("Digite um número:  "))
num2 = float(input('Digite outro:      '))
print(""" 
==== Informe que opção deseja ver ====
[1 - PAR OU ÍMPAR ]
[2 - POSITIVO OU NEGATIVO ]
[3 - INTEIRO OU DECIMAL ]
""")
opcao = input("Opção:  ")

if opcao == '1':
    if num1 % 2 == 0 and num2 % 2 == 0:
        print(f"{num1} e {num2} são números pares")
    elif num1 % 2 == 1 and num2 % 2 == 1:
        print(f"{num1} e {num2} são números ímpares")
    elif num1 % 2 == 0 or num2 % 2 == 1:
        print(f"{num1} é par e {num2} é ímpar")
    elif num1 % 2 == 1 or num2 % 2 == 0:
        print(f"{num1} é ímpar e {num2} é par")
if opcao == '2':
    if num1 > 0 and num2 > 0:
        print(f'Os números {num1} e {num2} são positivos')
    elif num1 < 0 and num2 < 0:
        print(f"Os números {num1} e {num2} são negativos")
    elif num1 > 0 or num2 < 0:
        print(f"O número {num1} é positivo e o {num2} é negativo")
    elif num1 < 0 or num2 > 0:
        print(f"O número {num1} é negativo e o {num2} é positivo")
if opcao == '3':
    if num1 == int(num1) and num2 == int(num2):
        print(f"Os número {num1:.0f} e {num2:.0f} são inteiros")
    elif num1 and num2:
        print(f"Os números {num1} e {num2} são decimais")
    # Não foram comparados se um ou outro é ou não decimal ou inteiro.