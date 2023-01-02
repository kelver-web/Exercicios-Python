# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

def temp_mes(*meses):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio',
            'junho', 'julho', 'agosto', 'setembro', 'outubro',
            'novembro', 'dezembro'
            ]

    lista_temp = []
    altas_temps = []
    meses_altas = []

    for i in meses:
        print(f'\nTEMPERATURA DO MÊS DE --> {i}:'.title())
        lista_temp.append(float(input('Temp C°:  ')))

        media_anual = sum(lista_temp) / len(lista_temp)

    for i in range(0, len(lista_temp)):
        if lista_temp[i] > media_anual:
            altas_temps.append(lista_temp[i])
            meses_altas.append(meses[i])
    return meses_altas



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
    test(temp_mes, ['janeiro', 'fevereiro', 'março', 'abril', 'maio',
            'junho', 'julho', 'agosto', 'setembro', 'outubro',
            'novembro', 'dezembro'], ['janeiro', 'julho', 'agosto', 'outubro', 'novembro', 'dezembro'])
    