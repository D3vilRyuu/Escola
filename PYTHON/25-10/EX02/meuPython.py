# Desenvolva um programa que pergunte a distância de uma viagem e calcule o preço da passagem,
# R$0,50 por KM em viagens até 200KM e R$0,45 em viagens acima de 200KM.

entrada = float(input('Digite a distancia da viagem'))

if entrada <= 200:
    valor = entrada * 0.50
    
if entrada > 200:
    valor = entrada * 0.45
    
print(f'o valor da viagem será de R${valor}')