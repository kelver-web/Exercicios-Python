# Escreva um programa que crie um dicionário com as notas de matemática, português e história de cinco alunos e depois imprima na tela a nota média de cada aluno.

alunos = {'Ana': {'matemática': 7, 'português': 8, 'história': 9},
          'João': {'matemática': 5, 'português': 6, 'história': 7},
          'Maria': {'matemática': 6, 'português': 7, 'história': 8},
          'Pedro': {'matemática': 8, 'português': 9, 'história': 10},
          'Carla': {'matemática': 9, 'português': 8, 'história': 7}
          }

for aluno, nota in alunos.items():
    media = sum(nota.values()) / len(nota)
    print(f"A média das notas de {aluno} é {media:.2f}")