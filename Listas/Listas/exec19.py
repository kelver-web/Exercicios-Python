# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a uma grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

print('QUAL O MELHOR SISTEMA OPERACIONAL PARA USO EM SERVIDORES?')
print('''
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
''')


votos = []
numero_votos = []
opcoes = ['Windowns Server', 'Unix', 'Linux', 'NetWare', 'MacOS', 'Outro']

while True:
    voto = int(input('Digite seu voto: '))
    votos.append(voto)

    if voto == 0:
        break
    
    elif voto > 6 or voto < 1:
        print('Voto invalido!')

print()
print('Sistema Operacional  Votos    %')
print('------------------   -----   ---')

for i in range(len(opcoes)):
    numero_votos.append(votos.count(i + 1))
    print(f'{opcoes[i]}        {votos.count(i + 1)}     {round(100 * votos.count(i + 1) / len(votos))}')
    
indice_ganhador = numero_votos.index(max(numero_votos))
print('\nO sistema mais votado foi o ', opcoes[indice_ganhador], ' com ', numero_votos[indice_ganhador], ' votos.')
