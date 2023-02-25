# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dias_semana = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira',
               'Quinta-Feira', 'Sexta-Feira', 'Sábado'
              ]

numero = int(input("Digite um número entre [1, 7] para ver o dia da semana:  "))

for i in range(len(dias_semana)):
    if numero == i + 1:
        dias = dias_semana[i]
    if numero > 7 or numero < 1:
        dias = 'Número inválido'

print(dias)