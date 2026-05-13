
while true: 
    
print ("=== SISTEMA DE VENDAS ===")
print ("1 - Registrar venda")
print ("2 - Ver resumo parcial")
print ("3 - Encerrar sistema")
print ("Escolha uma opção:")

opcao = int(input("Nome do produto"))


if opcao == 1
    nome = input("Nome do produto")
    valor_varejo = float(input("Valor unitário:"))
    quantidade = int(input("Quantidade:"))

    valor_bruto = valor_varejo * quantidade
    print("Valor: R$" (valor_bruto:))

    if valor_bruto < 100
        desconto = valor_bruto * 0

    if valor_bruto >= 100 and valor_bruto < 499.99
        desconto = valor_bruto * 0.05

    if valor_bruto >= 500 and valor_bruto < 999.99
        desconto = valor_bruto * 0.10
        valor_desconto - desconto

    else 
        desconto = valor_bruto * 0.15
        valor_desconto

valor_final = valor_bruto - desconto

vendas = +1


print("Valor inicial da venda: R$"(valor_bruto))
print("Desconto aplicado: R$"(valor_desconto))
print("Valor do desconto: R$"(desconto))
print("Valor final da venda: R$"(valor_final))
print("Venda registrada com sucesso!")

(print("=== SISTEMA DE VENDAS ==="))

print("1- Registrar venda")
print("2- Ver resumo parcial")
print("3- Encerrar sistema")

print("Escolha uma")

elif opcao == 2:

        print("=== RESUMO PARCIAL ===")

        print("Total de vendas realizadas:", vendas)
        print("Total bruto vendido: R$", valor_bruto)
        print("Total de descontos concedidos: R$", desconto)
        print("Total líquido vendido: R$", valor_final)
