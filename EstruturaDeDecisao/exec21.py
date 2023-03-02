# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

print("======== Caixa Eletrônico ========")

saque = float(input("Informe o valor:  "))

if saque > 600:
    print("Valor máximo de R$600.00")
elif saque < 10:
    print("Valor mínimo de R$10.00")
else:
    cem = saque // 100
    saque = saque - (cem * 100)
    cinquenta = saque // 50
    saque = saque - (cinquenta * 50)
    dez = saque // 10
    saque = saque - (dez * 10)
    cinco = saque // 5
    saque = saque - (cinco * 5)
    um = saque // 1
    saque = saque - (um * 1)
    if cem > 0:
        print(f"{cem:.0f} nota(s) de cem")
    if cinquenta > 0:
        print(f"{cinquenta:.0f} nota(s) de cinquenta")
    if dez > 0:
        print(f"{dez:.0f} nota(s) de dez")
    if cinco > 0:
        print(f"{cinco:.0f} nota(s) de cinco")
    if um > 0:
        print(f"{um:.0f} nota(s) de um")