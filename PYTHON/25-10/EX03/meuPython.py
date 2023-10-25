# Faça um programa que leia 3 numeros inteiros e qual o maior e qual o menor.

a = int(input('Digite um numero'))
b = int(input('Digite o segundo numero'))
c = int(input('Digite o terceiro numero'))

# Para definir o menor

menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#  Para definir o maior

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# Aparecer na tela

print(f'O maior numero é o {maior}')
print(f'O menor numero é o {menor}')