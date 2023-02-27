# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

'''ax2 + bx + c = 0'''

from math import sqrt

a = int(input("Valor de a:  "))
if a == 0:
    print("Essa equação não é do 2º grau")
else:
    b = int(input("Valor de b:  "))
    c = int(input("Valor de c:  "))

print(f"a = {a}, b = {b}, c = {c}")

Δ = b ** 2 - 4 * a * c

if Δ < 0:
    print("Essa equação não possiu raizes reais.")

else:
    x1 = (- b + sqrt(Δ)) / 2 * a
    x2 = (- b - sqrt(Δ)) / 2 * a
if Δ == 0:
    print(f"1 raiz real {x1:.2f}")
else:
    print(f"2 raizes reais, x1 = {x1:.0f}, x2 = {x2:.0f}")
