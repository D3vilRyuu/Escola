# 4- Crie um programa que peça ao usuário um número positivo, e faça a contagem de quantos números pares existem,
# de 0 ao número informado.

numero = int(input("Digite um número positivo: "))
contagem_pares = 0

if numero < 0:
    print("Por favor, digite um número positivo.")
else:
    contador = 0
    while contador <= numero:
        if contador % 2 == 0:
            contagem_pares += 1
        contador += 1

print(f"Existem {contagem_pares} números pares de 0 a {numero}.")


        

