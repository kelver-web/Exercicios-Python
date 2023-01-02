# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Informe o valor hora:  '))
horas_trabalhadas = float(input('Informe as horas trabalhadas:  '))
total = valor_hora * horas_trabalhadas

print(f'Total a ganhar R${total:.2f}')
