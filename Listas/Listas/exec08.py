# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.


lista_idade = []
lista_altura = []

for i in range(1, 3):
    print(f'Dados da {i}º pessoa')
    idade = int(input('Idade: '))
    lista_idade.append(idade)
    altura = float(input('Altura: '))
    lista_altura.append(altura)

print(f'Idade em ordem decrescente: {lista_idade[::-1]}')
print(f'Altura em ordem decrescente: {lista_altura[::-1]}')

