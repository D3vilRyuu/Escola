destino = input("Qual é o seu destino? \n 1-Londres: Diária $150 Extra: Zoológico: $30 \n 2-París: Diária $200 Extra: Zoológico: $40\n 3-México: Diária $100 Extra: Zoológico: $30 \n R: ")
quant_dias = int(input("Quantos dias pretende passar? \n R: "))
ativ_extra = input("Tem interesse em atividades extras?SIM ou NAO \n R:")

if destino == "1":
    preco_hosp = 150 * quant_dias
    if ativ_extra == "SIM":
        preco_total = preco_hosp + 30
        print(f"O preço total com atividade extra será de ${preco_total}.")
    else:
        print(f"O preço total sem atividade extra só a hospedagem será de ${preco_hosp}.")
elif destino == "2":
    preco_hosp = 200 * quant_dias
    if ativ_extra == "SIM":
        preco_total = preco_hosp + 40
        print(f"O preço total com atividade extra será de ${preco_total}.")
    else:
        print(f"O preço total sem atividade extra só a hospedagem será de ${preco_hosp}.")
else:
    preco_hosp = 100 * quant_dias
    if ativ_extra == "SIM":
        preco_total = preco_hosp + 30
        print(f"O preço total com atividade extra será de ${preco_total}.")
    else:
        print(f"O preço total sem atividade extra só a hospedagem será de ${preco_hosp}.")