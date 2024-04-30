# Escreva um programa que receba um número e verifica se ele é positivo, e ímpar.

numero = input("Digite um numero: ")
numero = (int(numero))

if numero  > 0 and numero % 2 != 0:
    print("Seu numero é impar e positivo")
else:
    print("Seu numero não é impar e positivo")