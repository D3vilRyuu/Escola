# Crie um programa que leia um numero inteiro e diga se o numero é impar ou par: (usando %)

num = int(input('Digite um numero'))
resto = num % 2

if resto == 0:
    print('Numero é par')
else:
    print('Numero é impar')
