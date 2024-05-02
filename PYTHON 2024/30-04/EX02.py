#Escreva um programa que receba a idade de uma pessoa e retorne se ela é OBRIGADA a votar nas eleições.

idade = input("Qual é sua idade? \n R: ")
idade = (int(idade))

if idade >= 18 and idade <= 70:
    print("Você é obrigado(a) a votar por conta da sua idade")
else:
    print("Não é obritagório o seu voto!!")
