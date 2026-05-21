vendas = 0
total_bruto = 0
total_descontos = 0
total_liquido = 0

while True:

    print("=== SISTEMA DE VENDAS ===")
    print("1 - Registrar venda")
    print("2 - Ver resumo parcial")
    print("3 - Encerrar sistema")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome do produto: ")
        valor_varejo = float(input("Valor unitário: "))
        quantidade = int(input("Quantidade: "))

        valor_desconto = 0
        valor_bruto = valor_varejo * quantidade
        print("Valor: R$", valor_bruto)

        if valor_bruto < 100:
            desconto = valor_bruto * 0

        elif valor_bruto >= 100 and valor_bruto < 499.99:
            desconto = valor_bruto * 0.05

        elif valor_bruto >= 500 and valor_bruto < 999.99:
            desconto = valor_bruto * 0.10
            valor_desconto = desconto

        else:
            desconto = valor_bruto * 0.15
            valor_desconto = desconto

        valor_final = valor_bruto - desconto

        vendas += 1
        total_bruto += valor_bruto
        total_descontos += desconto
        total_liquido += valor_final

        print("Valor inicial da venda: R$", valor_bruto)
        print("Desconto aplicado: R$", valor_desconto)
        print("Valor do desconto: R$", desconto)
        print("Valor final da venda: R$", valor_final)
        print("Venda registrada com sucesso!")

    elif opcao == 2:
        print("=== RESUMO PARCIAL ===")

        print("Total de vendas realizadas:", vendas)
        print("Total bruto vendido: R$", total_bruto)
        print("Total de descontos concedidos: R$", total_descontos)
        print("Total líquido vendido: R$", total_liquido)

    elif opcao == 3:

        print("=== RESUMO FINAL ===")

        print("Total de vendas realizadas:", vendas)
        print("Total bruto vendido: R$", total_bruto)
        print("Total de descontos concedidos: R$", total_descontos)
        print("Total líquido vendido: R$", total_liquido)

        break

    else:

        print("Escolha uma opção válida.")