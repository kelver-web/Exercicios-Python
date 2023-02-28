# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print("Verificação de datas")

data = input("Data: ")

if int(data[:2]) != 0 and int(data[:2]) <= 31: # Verifica dia e cai no próximo if
    if int(data[3:5]) != 0 and int(data[3:5]) <= 12: # Verifica mês e cai no próximo if
        if int(data[6:11]) != 0: # Verifica ano e se tudo estiver certo print normal
            print("Data Válida!")
        else:
            print("Data Inválida")
    else:
        print("")
        print("Data Inválida")
else:
    print("")
    print("Data Inválida")