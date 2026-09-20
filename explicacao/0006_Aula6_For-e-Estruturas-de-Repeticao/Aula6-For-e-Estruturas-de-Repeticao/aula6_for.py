for i in range(10):
    print("Se inscreva no canal")


lista_precos = [1500, 1000, 800, 2000]

# taxa_imposto = 0.1

# for preco in lista_precos:
#     imposto = preco * taxa_imposto
#     print(f"Preço do produto {preco}, imposto é de {imposto}")

# Exemplo 1
# produtos de até 1000 pagam 10%
# produtos acima de 1000 pagam 15% de imposto

# for preco in lista_precos:
#     if preco > 1000:
#         taxa = 0.15
#     else:
#         taxa = 0.1
#     imposto = taxa * preco
#     print(f"Preço do produto: {preco}, Imposto: {imposto}")

# Exemplo 2:
# mesma regra de imposto mas eu quero conseguir calcular o total de imposto somado de todos os produtos

# total_imposto = 0

# for preco in lista_precos:
#     if preco > 1000:
#         taxa = 0.15
#     else:
#         taxa = 0.1
#     imposto = taxa * preco

#     total_imposto = total_imposto + imposto
    
#     print(f"Preço do produto: {preco}, Imposto: {imposto}")

# print("Total de imposto", total_imposto)

vendas_23 = {"jan": 15000, "fev": 10000, "mar": 5000}
vendas_24 = {"jan": 16000, "fev": 11000, "mar": 5100}

# calculo percentual de crescimento
# 16000 / 15000 - 1 -> qnts % eu cresci de um ano para o outro

for mes in vendas_24:
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes]
    crescimento = valor_24 / valor_23 - 1
    print(f"No mês de {mes} o crescimento foi de {crescimento:.1%}")



