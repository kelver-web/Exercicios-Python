# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação Python. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
# O total de votos computados;
# Os númeos e respectivos votos de todos os jogadores que receberam votos;
# O percentual de votos de cada um destes jogadores;
# O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
# Enquete: Quem foi o melhor jogador?

# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50
# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0

# Resultado da votação:

# Foram computados 8 votos.

# Jogador Votos           %
# 9               4               50,0%
# 10              3               37,5%
# 11              1               12,5%
# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

lista_jogadores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,
                   14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

lista_votos = []
mais_votados = []
numero_mais_votado = []


print('Enquete: Quem foi o melhor jogador?\n')
while True:
    num_jogador = int(input('Número do jogador (0=fim):  '))

    if num_jogador == 0:
        break

    if num_jogador not in lista_jogadores:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    
    lista_votos.append(num_jogador)
    for voto in lista_votos:
        if voto > len(lista_jogadores):
            lista_votos.pop()
            
print()
print(f'Foram computados {len(lista_votos)} votos.\n')
contador = 0
for i in range(0, len(lista_jogadores)):
    if contador not in lista_votos:
        contador += 1
        
    else:
        mais_votados.append(lista_votos.count(contador))
        numero_mais_votado.append(contador)
        contador += 1

print()
print('Resultado da votação:\n')
try:
    melhor = mais_votados.index(max(mais_votados))
    print('Jogador      Votos       %')
    for i in range(0, len(numero_mais_votado)):
        print(f'{numero_mais_votado[i]}            {mais_votados[i]}           {100 * mais_votados[i] / len(lista_votos):.2f}')
    print(f"O melhor jogador foi o número {numero_mais_votado[melhor]} com {mais_votados[melhor]} votos conrespondendo a {100 * mais_votados[melhor] / len(lista_votos):.0f}% dos votos\n")
except ValueError:
    melhor = 0