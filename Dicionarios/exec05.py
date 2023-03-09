# Escreva uma função que receba uma lista de dicionários como parâmetro, onde cada dicionário representa uma pessoa com as informações de nome e idade, e retorne a lista ordenada por idade.


def func(x):
    return sorted(x, key=lambda x: x['idade'])

lista_dict = [{'nome': 'Maria', 'idade': 16}, {'nome': 'Rita', 'idade': 20}]
print(func(lista_dict))