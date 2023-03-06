"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar."""

print("""
============== O Hipermercado Tabajara ===============
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
======================================================
""")
print("""
[1] Filé Duplo
[2] Alcatra
[3] Picanha
""")

opcao = int(input("Informe qual o tipo da carne:  "))
quantidade = float(input("Quantidade:  "))
carne = None


if opcao == 1:
    if quantidade <= 5:
        preco = quantidade * 4.90
        total = preco
        carne = 'Filé Duplo'
    
    else:
        preco = quantidade * 5.80
        total = preco
    
if  opcao == 2:
    if quantidade <= 5:
        preco = quantidade * 5.90
        total = preco
        carne = 'Alcatra'

    else:
        preco = quantidade * 6.80
        total = preco

if opcao == 3:
    if quantidade <= 5:
        preco = quantidade * 6.90
        total = preco
        carne = 'Picanha'

    else:
        preco = quantidade * 7.80
        total = preco
print()
pagamento = print("""===== Forma de pagamento =====
[D] Dinheiro
[C] Cartão
""")

tipo_pag = input("Tipo de pagamento:  ")
if tipo_pag in "Dd":
    print(
        f"\n========== CUPOM FISCAL ==========="
        f"\nTipo Prod: -----> {carne}"
        f"\nQuant: ---------> {quantidade:.0f}Kg"
        f"\nPreço Total ----> {total:.2f}"
        f"\nTipo Pag    ----> [{tipo_pag}] Dinheiro"
        f"\nDesconto    ----> 00.00"
        f"\nTotal a pagar --> {total:.2f}"
    )
  
elif tipo_pag in "Cc":
    print(
        f"\n========== CUPOM FISCAL ==========="
        f"\nTipo Prod: -----> {carne}"
        f"\nQuant: ---------> {quantidade:.0f}Kg"
        f"\nPreço Total ----> {total:.2f}"
        f"\nTipo Pag    ----> [{tipo_pag}] Cartão"
        f"\nDesconto    ----> {total * 0.05:.2f}"
        f"\nTotal a pagar --> {total - (total * 0.05):.2f}"
    )
