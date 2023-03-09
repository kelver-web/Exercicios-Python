# Escreva uma função que receba um dicionário como parâmetro e retorne a soma de todos os valores do dicionário.

def soma_valores(x):
    '''Retorna a soma dos valores do dicionário.'''
    soma = x.values()
    return sum(soma)

dict_valores = {'um': 1, 'dois': 2, 'tres': 3, 'novecentos': 900}
print(soma_valores(dict_valores))