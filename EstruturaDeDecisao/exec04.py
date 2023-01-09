# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra:  ').lower()

if letra in 'aeiou':
    print(f'Vogal')
else:
    print(f'Consoante')