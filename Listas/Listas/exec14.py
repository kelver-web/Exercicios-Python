# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

lista_perguntas = ["Telefonou para a vítima? [s/n]: ", "Esteve no local do crime? [s/n]: ", "Mora perto da vítima? [s/n]: ",
                   "Devia para a vítima? [s/n]: ", "Já trabalhou com a vítima? [s/n]: "]
respostas = []
sim = []
nao = []

print("=== Interrogatório ===\n")
for perguntas in lista_perguntas:
    respostas.append(input(f'{perguntas}'))

for resposta in respostas:
    if resposta in 's':
        sim.append(resposta)
    else:
        nao.append(resposta)
    
if len(sim) > 1 and len(sim) < 3:
    print("Suspeito")
elif len(sim) >= 3 and len(sim) <= 4:
    print("Cumplice")
elif len(sim) > 4:
    print("Assassino")
else:
    print('Inocente')
    
