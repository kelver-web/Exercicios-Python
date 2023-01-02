# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_quadrado = []

# for x in lista:
#     x *= x
#     lista_quadrado.append(x)
# print(sum(lista_quadrado))

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_quadrado = [x ** 2 for x in lista]
# print(sum(list_quadrado))


def lista_quadrado(lista):
    lista = [x ** 2 for x in lista]
    return sum(lista)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, num, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(num)

    if out == expected:
        sign = '\033[36m ✅\033[m'
        info = ''
    else:
        sign = '\033[31m ❌\033[m'
        info = f'e o correto é {expected}'

    print(f"{sign} {f.__name__}({num}) retornou '{out}' {info}")


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(lista_quadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 385)
    