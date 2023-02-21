# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#  Salário Bruto: (5 * 220)        : R$ 1100,00
#  (-) IR (5%)                     : R$   55,00  
#  (-) INSS ( 10%)                 : R$  110,00
#  FGTS (11%)                      : R$  121,00
#  Sindicato (3%)                  : R$  00.00
#  Total de descontos              : R$  165,00
#  Salário Liquido                 : R$  935,00

valor_horas: float = float(input("Valor horas trabalhadas:  "))
quantidade_horas: float = float(input("Quantidade horas: "))

valor_salario_bruto: float = valor_horas * quantidade_horas

if valor_salario_bruto <= 900:
    desconto_ir: float = 0.0

elif valor_salario_bruto > 900 and valor_salario_bruto <= 1500:
    desconto_ir: float = 5

elif  valor_salario_bruto > 1500 and valor_salario_bruto <= 2500:
    desconto_ir: float = 10

else:
    desconto_ir: float = 20


ir: float = valor_salario_bruto * (desconto_ir / 100)
inss: float = valor_salario_bruto * (10 / 100)
fgts: float = valor_salario_bruto * (11 / 100)
sindicato: float = valor_salario_bruto * (3 / 100)
total_descontos: float = ir + inss + sindicato
salario_liquido: float = valor_salario_bruto - total_descontos


print(
    f"\nSalário Bruto     :R${valor_salario_bruto:.2f}"
    f"\n(-) IR (5%)       :R${ir:.2f}"
    f"\n(-) INSS (10%)    :R${inss:.2f}"
    f"\nFGTS (11%)        :R${fgts:.2f}"
    f"\nSindicato (3%)    :R${sindicato:.2f}"
    f"\nTotal de descontos:R${total_descontos:.2f}"
    f"\nSalário Liquido   :R${salario_liquido:.2f}"
)
