idade = 15

if idade >= 18:
    print("A pessoa é maior de idade")
else:
    print("A pessoa é menor de idade")



# Notas e faltas cumprem o critério.
nota_aluno = 7
quant_faltas = 4

if nota_aluno >= 8 and quant_faltas <= 5:
    print("O aluno está apto para a excursão")
else:
    print("O aluno não está apto para a excursão")

# Uma agência de shows estão desenvolvendo um sistema para verificar se os clientes podem
# pagar meia entrada , Para pagar meia entrada, o cliente deve ser:
# Estudantes: Tem que estar matriculado em uma instituição de ensino
# Idoso: Idade acima de 65 anos

status_ensino = input("Está matriculado em uma instituição de ensino? \n 1 - Sim \n 2 - Não \n")
status_ensino = (int(status_ensino))

idade_cliente = input("Qual é sua idade? ")
idade_cliente = (int(idade_cliente))

if status_ensino == 1 or idade_cliente >= 65:
    print("Você pode comprar uma meia entrada!")
else: 
    print("Você está não pode comprar uma meia entrada!")

