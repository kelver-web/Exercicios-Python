# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


print("""
==== Bem vindo aos Postos Bertodo ====
A - alcool
G - gasolina
""")
opcao = input("Tipo de combustível:  ")
if not opcao in "Aa" and not opcao in "Gg":
    print("Opção inválida!")

if opcao in  "Aa":
    print("ÁLCOOL")
    litros = float(input("Litros:  "))
    if litros <= 20:
        preco = litros * 1.90
        desconto = preco * 0.03
        total = preco - desconto
        print(f"Total -> R${total:.2f}")
    else:
        preco = litros * 1.90
        desconto = preco * 0.05
        total = preco - desconto
        print(f"Total -> R${total:.2f}")

if  opcao in "Gg":
    print("GASOLINA")
    litros = float(input("Litros:  "))
    if litros <= 20:
        preco = litros * 2.50
        desconto = preco * 0.04
        total = preco - desconto
        print(f"Total -> R${total:.2f}")
    else:
        preco = litros * 2.50
        desconto = preco * 0.06
        total = preco - desconto
        print(f"Total -> R${total:.2f}")
