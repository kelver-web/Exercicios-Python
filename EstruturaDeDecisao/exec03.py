# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite uma letra:  ").lower()

if letra in 'f':
    print('F - Feminino')
elif letra in 'm':
    print('M - Masculino')
else:
    print('Sexo Inválido')