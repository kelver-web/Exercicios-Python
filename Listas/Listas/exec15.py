# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d. Calcule e mostre a soma dos valores;
# e. Calcule e mostre a média dos valores;
# f. Calcule e mostre a quantidade de valores acima da média calculada;
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# h. Encerre o programa com uma mensagem;


notas = []
acima_da_media = []
abaixo_de_sete = []

while True:
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    
    if nota == -1:
        notas.pop()
        break
media = sum(notas) / len(notas)
inverso = notas[::-1]

for i in notas:
    if i > media:
        acima_da_media.append(i)

for i in notas:
    if i < 7:
        abaixo_de_sete.append(i)

print()
print(f'Foram lidas {len(notas)} notas')
print(f'Valores em ordem de informação: {notas}')
print("Valores em ordem inversa:")
for i in inverso:
    print(i)

print(f"Soma de todas as notas ---> {sum(notas)}")
print(f"A média de notas é ---> {media}")
print(f"Quantidade de notas acima da média ---> {len(acima_da_media)}")
print(f"Quantidade de notas a baixo de 7 ---> {len(abaixo_de_sete)}\n")
print('Obrigado por user o nosso sistema.')