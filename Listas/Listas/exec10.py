# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.




def sum_listas(lista1, lista2):
    lista1 = [x for x in range(1, 11)]
    lista2 = [s for s in range(11, 21)]
    lista3 = lista1 + lista2
    return lista3


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, num, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*num)

    if out == expected:
        sign = '\033[36m ✅\033[m'
        info = ''
    else:
        sign = '\033[31m ❌\033[m'
        info = f'e o correto é {expected}'

    print(f"{sign} {f.__name__}({num}) retornou '{out}' {info}")


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(sum_listas, ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17 ,18, 19, 20]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ,18, 19, 20])
    