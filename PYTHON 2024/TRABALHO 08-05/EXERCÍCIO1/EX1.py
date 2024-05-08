produto = int(input("Qual produto vc deseja comprar? (Apenas um no momento)\n 1-Mouse: Preço Uni. R$20 \n 2-Teclado: Preço Uni. R$10 \n 3-Monitor: Preço Uni. R$320 \n R: "))
quant_produtos = int(input("Qual a quantidade que deseja?"))

if produto == 1:
    subtotal_mouse = 20 * quant_produtos
    continuar = input("Você deseja continuar comprando?")
    if continuar == "SIM":
        produto = int(input("Qual produto vc deseja comprar? (Apenas um no momento)\n 2-Teclado: Preço Uni. R$10 \n 3-Monitor: Preço Uni. R$320 \n R: "))
        quant_produtos = int(input("Qual a quantidade que deseja?"))
        if produto == 2:
            subtotal_teclado = 10 * quant_produtos
            total = subtotal_mouse + subtotal_teclado
            if total > 1000:
                desconto = total - (total * 0.10)
                print(f"A compra total com desconto ficará: R${desconto}")
            else:
                print(f"A compra total sem desconto dará: R${total}")
        else:
            subtotal_monitor = 320 * quant_produtos
            total = subtotal_mouse + subtotal_monitor
            
            if total > 1000:
                desconto = total - (total * 0.10)
                print(f"A compra total com desconto ficará: R${desconto}")
            else:
                print(f"A compra total sem desconto dará: R${total}")
    else:
        print(f"Preço: R${subtotal_mouse}")
elif produto == 2:
    subtotal_teclado = 10 * quant_produtos
    continuar = input("Você deseja continuar comprando?")
    if continuar == "SIM":
        produto = int(input("Qual produto vc deseja comprar? (Apenas um no momento)\n 1-Mouse: Preço Uni. R$20 \n 3-Monitor: Preço Uni. R$320 \n R: "))
        quant_produtos = int(input("Qual a quantidade que deseja?"))
        if produto == 1:
            subtotal_mouse = 20 * quant_produtos
            total = subtotal_mouse + subtotal_teclado
            
            if total > 1000:
                desconto = total - (total * 0.10)
                print(f"A compra total com desconto ficará: R${desconto}")
            else:
                print(f"A compra total sem desconto dará: R${total}")
        else:
            subtotal_monitor = 320 * quant_produtos
            total = subtotal_teclado + subtotal_monitor
            
            if total > 1000:
                desconto = total - (total * 0.10)
                print(f"A compra total com desconto ficará: R${desconto}")
            else:
                print(f"A compra total sem desconto dará: R${total}")
    else:
        print(f"Preço: R${subtotal_teclado}")
else:
    subtotal_monitor = 320 * quant_produtos
    continuar = input("Você deseja continuar comprando?")
    if continuar == "SIM":
        produto = int(input("Qual produto vc deseja comprar? (Apenas um no momento)\n 1-Mouse: Preço Uni. R$20 \n 2-Teclado: Preço Uni. R$10 \n R: "))
        quant_produtos = int(input("Qual a quantidade que deseja?"))
        if produto == 1:
            subtotal_mouse = 20 * quant_produtos
            total = subtotal_mouse + subtotal_monitor
            desconto = total * 0.10
            total_desconto = total - desconto
            if total > 1000:
                print(f"A compra total com desconto ficará: R${total_desconto}")
            else:
                print(f"A compra total sem desconto dará: R${total}")

        else:
            subtotal_teclado = 10 * quant_produtos
            total = subtotal_teclado + subtotal_monitor
            desconto = total * 0.10
            total_desconto = total - desconto
            if total > 1000:
                print(f"A compra total com desconto ficará: R${total_desconto}")
            else:
                print(f"A compra total sem desconto dará: R${total}")
    else:
        print(f"Preço: R${subtotal_monitor}")


