# Faça um programa que pergunte o preço de três produtos e informe qual produto
# você deve comprar, sabendo que a decisão é sempre pelo mais barato

produtos = [float(input(f'Preço do {x+1}º produto:  ')) for x in range(3)]
print(f"Baseando-se no preço do produto mais barato, você deve comprar o de \
valor R${min(produtos):.2f}")
