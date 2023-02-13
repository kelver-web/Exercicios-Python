# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.



print("""
M-matutino
V-vespertino
N-noturno
""")
print("Em qual turno você estuda?")
turno: str  = input("Turno:  ")

if turno in "mM":
    print("Bom dia!")
elif turno in "vV":
    print("Boa tarde!")
elif turno in "nN":
    print("Boa noite!")
else:
    print("Turno inválido")