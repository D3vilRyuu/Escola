# 1- Escreva um programa que solicite ao usuário um número inteiro positivo e, em seguida, exiba uma contagem
# regressiva a partir desse número até zero.

num = int(input("Digite um número inteiro positivo: "))

while num > 0:
    num = num - 1
    print(num)