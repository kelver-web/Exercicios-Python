# Escreva um programa que crie um dicionário com os nomes e notas de dez alunos, calcule a média das notas e imprima na tela.

pessoas = { 'Caio': 5.5,  'Maria': 7.0,  'Rita': 8.0, 
            'Cintia': 9.0,  'Paula': 10.0,  'Marcos': 6.0,
            'João': 8.0,  'Ricardo': 7.8,  'Estela': 6.6,
            'Marta': 7.5}

media = sum(pessoas.values()) / len(pessoas)
print(f"A média da da turma foi de: {media:.2f}")