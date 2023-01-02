# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
# consoantes foram lidas. Imprima as consoantes.

# array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
# cont = 0
# for i in array:
#     if i in 'bcdfghjk':
#         consoantes = i
#         cont += 1
#         print(f'{consoantes}', end=' ')
# print(f'\nForam lidas {cont} consoantes')

# array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
# consoantes = [i for i in array if i in 'bcdfghjk']
# tamanho = len(consoantes)
# print(f'As consoantes lisdas foram: {consoantes}')
# print(f'Total consoantes: {tamanho}')

array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
consoantes = list(filter(lambda x: x in 'bcdfghjk', array))
print(f'Consoantes lidas: {[i for i in consoantes]}')
print(f'Total consoantes: {len(consoantes)}')
