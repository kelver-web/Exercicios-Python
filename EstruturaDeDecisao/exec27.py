"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

print("""============= Promoção de fim de semana ==============
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

""")
      
print('''=== Frutas da tabela ===
[1] Maçã
[2] Morango''')

opcao = input('Digite um opção: ')
quant = float(input('Informa a quantidade em KG: '))
if opcao == '1':
    print('Você escolheu Maçã-> 1.80 por KG até 5Kg')
    print('Compre acima de 5Kg e pague apenas 1.50')
    print('Acima de 8kg ou R$25.00 em compras ganhe 10%')

    if quant <= 5:
        maca1 = quant * 1.80
        print('você comprou a preço normal')
        print(f'Total: {quant}kg = R$----> {maca1:.2f}')

    elif quant > 5 and quant <= 8:
        maca2 = quant * 1.50
        print('Você comprou com desconto')
        print(f'Total: {quant}kg = R$----> {maca2:.2f}')

    elif quant > 8:
        maca2 = quant * 1.50
        desconto = maca2 * 0.10
        total = maca2 - desconto
        print('Você comprou com desconto de 10%')
        print(f'Total: {quant}kg = R$---->{total:.2f}')

    elif maca2 > total:
        maca2 = quant * 1.50
        desconto = maca2 * 0.10
        total = maca2 - desconto
        print('Você comprou com desconto de 10%')
        print(f'Total: {quant}kg = R$---->{total:.2f}')


if opcao == '2':
    print('Você escolheu Morango-> 2.50 por KG até 5Kg')
    print('Compre acima de 5Kg e pague apenas 2.20')
    print('Acima de 8kg ou R$25.00 em compras ganhe 10%')

    if quant <= 5:
        morango1 = quant * 2.50
        print('Você comprou a preço normal')
        print(f'Total: {quant}kg = R$----> {morango1:.2f}')

    elif quant > 5 and quant <= 8:
        morango2 = quant * 2.20
        print('Você comprou com desconto')
        print(f'Total: {quant}kg = R$----> {morango2:.2f}')

    elif quant > 8:
        morango2 = quant * 2.20
        desconto = morango2 * 0.10
        total = morango2 - desconto
        print('Você comprou com desconto de 10%')
        print(f'Total: {quant}kg = R$---->{total:.2f}')

    elif morango2 > total:
        morango2 = quant * 1.50
        desconto = morango2 * 0.10
        total = morango2 - desconto
        print('Você comprou com desconto de 10%')
        print(f'Total: {quant}kg = R$---->{total:.2f}')