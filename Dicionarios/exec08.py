# Escreva um programa que crie um dicionário com os nomes e salários de cinco funcionários de uma empresa, calcule o valor total que a empresa gatsta com os salários e imprima na tela.

empregados = {'Ailton': 2000, 'Marcos': 1350, 'Rita': 1500, 'Jurema': 1800, 'Marta': 1450}
total = sum(empregados.values())
print(f"Total salarial R${total}")