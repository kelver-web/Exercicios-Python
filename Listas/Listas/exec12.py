# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


# idades = []
# alturas = []
# cont = 0

# for i in range(3):
#     idades.append(int(input('Idade: ')))
#     alturas.append(float(input("Altura: ")))

# media = sum(alturas) / len(alturas)

# for i in range(0, len(idades)):
#     if idades[i] > 13 and alturas[i] < media:
#         cont += 1

# print(f'Média: {media:.2f}')
# print(f"Alunos com + 13 anos abaixo da média: {cont}")

def media_alunos(idades, alturas):
    idades = [10, 15, 9, 22, 13, 12, 14]
    alturas = [1.60, 1.35, 1.76, 1.98, 1.77, 1.66, 1.80]
    media = sum(alturas) / len(alturas)

    cont = 0

    for i in range(len(idades)):
        if idades[i] > 13 and alturas[i] < media:
            cont += 1
    return cont


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
    test(media_alunos, ([10, 15, 9, 22, 13, 12, 14], [1.60, 1.35, 1.76, 1.98, 1.77, 1.66, 1.80]), 1)
    