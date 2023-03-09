# Escreva uma função que receba um dicionário como parâmetro e retorne uma lista de tuplas contendo os pares chave-valor do dicionário.



def func(x):
    return x.items()

dicionario = {'nome': 'Maria', 'idade': 15, 'altura': 165}

print(func(dicionario))