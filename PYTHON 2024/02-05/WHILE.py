# Programa que irá executar uma contagem(contador)

# O programa irá executar uma contagem e exibir o numero atual na tela(10)

contador = 0

# Enquanto contador for menor ou igual a 10

while contador <= 10:
    print(f"Numero atual: {contador}")
    contador += 1
    contador = contador + 1

# Contador que mostre todos os numeros pares até 100
contador2 = 2
print("CONTADOR DE PARES (0 - 100)")


while contador2 <= 100:
    print(f"Numero atual: {contador2}")
    contador2 += 2
    # contador = contador + 2

# Contador regressivo que irá contar de forma descrescente de 0 a 10

contador3 = 10
print("CONTADOR REGRESSIVO")

while contador3 >= 0:
    print(f"Numero atual: {contador3}")
    contador3 -= 1