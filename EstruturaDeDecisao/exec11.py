# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario: float = float(input("Salário:  "))

if salario <= 280:
    porcentual_aumento = 20
    valor_aumento: float = salario * 0.20
    porcento: float = salario + (salario * 0.20)
    print(f'Salário antes do reajuste ----- R${salario:.2f}')
    print(f'Porcentual aplicado       ----- {porcentual_aumento}%')
    print(f'Valor do aumento -        ----- R${valor_aumento:.2f}')
    print(f'Novo salário              ----- {porcento:.2f}')

elif salario > 280 and salario <= 700:
    porcentual_aumento = 15
    valor_aumento: float = salario * 0.15
    porcento: float = salario + (salario * 0.15)
    print(f'Salário antes do reajuste ----- R${salario:.2f}')
    print(f'Porcentual aplicado       ----- {porcentual_aumento}%')
    print(f'Valor do aumento -        ----- R${valor_aumento:.2f}')
    print(f'Novo salário              ----- {porcento:.2f}')
    quinze_porcento: float = salario + (salario * 0.15)

elif salario > 700 and salario <= 1500:
    porcentual_aumento = 10
    valor_aumento: float = salario * 0.10
    vinte_porcento: float = salario + (salario * 0.10)
    print(f'Salário antes do reajuste ----- R${salario:.2f}')
    print(f'Porcentual aplicado       ----- {porcentual_aumento}%')
    print(f'Valor do aumento -        ----- R${valor_aumento:.2f}')
    print(f'Novo salário              ----- {vinte_porcento:.2f}')
    dez_porcento: float = salario + (salario * 0.10)

elif salario > 1500:
    porcentual_aumento = 5
    valor_aumento: float = salario * 0.05
    vinte_porcento: float = salario + (salario * 0.05)
    print(f'Salário antes do reajuste ----- R${salario:.2f}')
    print(f'Porcentual aplicado       ----- {porcentual_aumento}%')
    print(f'Valor do aumento          ----- R${valor_aumento:.2f}')
    print(f'Novo salário              ----- {vinte_porcento:.2f}')
    cinco_porcento: float = salario + (salario * 0.05)
    


