# Escreva um programa que leia a velocidade de um veiculo se ele utrapassar 80KM/h mostre a mensagem
# Dizendo que ele foi multado e a multa vai custar R$ 7,00 por cada KM acima do limite.

velo = int(input('Qual a velocidade?'))

if velo > 80:
    multa = (velo - 80) * 7
    print(f'Voce utrapassou a velocidade permitida de 80KM/h e sera multado por isso sua velocidade foi {velo} sua multa será de R${multa}') 
else:
    print(f'Continue andando assim, se ultrapassar a velocidade de 80KM/h sera multado em R$7,00 cada KM')