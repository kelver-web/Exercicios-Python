'''
Crie um dicionário com as chaves sendo os dias da semana (segunda, terça, quarta, quinta, sexta, sábado, domingo) e os valores sendo o número correspondente do dia da semana (1, 2, 3, 4, 5, 6, 7) e mostre em sequencia os dias um abaixo do outro.
'''

dias_semana = {'domingo': 1, 'segunda': 2, 'terça': 3, 'quarta': 4, 'quinta': 5, 'sexta': 6, 'sabado': 7}
dia = list(dias_semana.items())
for i in dia:
    print(i[0])