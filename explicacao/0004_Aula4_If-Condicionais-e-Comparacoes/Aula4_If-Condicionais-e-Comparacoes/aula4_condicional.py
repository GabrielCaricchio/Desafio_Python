faturamento = 1000
custo = 600

lucro = faturamento - custo

# if condicao/comparação:
#     # o que eu quero que aconteça se essa condição for verdadeira
# else:
#     # o que eu quero que aconteça se essa condição for falsa

if lucro >= 0:
    print("Lucro de", lucro)
    print("Deu lucro")
else:
    print("Prejuízo de", lucro)
    print("Deu prejuízo")

print("Acabou")

# Exemplo:
# produtos = ["iphone", "ipad", "airpod"]
# novo_produto = input("Digite o nome do produto:")

# if novo_produto in produtos:
#     print("Produto já existente")
# else:
#     print(f"{novo_produto} cadastrado com sucesso")
#     produtos.append(novo_produto)

# print(produtos)

# Exemplo 2:
# bonus dos funcionários
# vendas maiores do que 15000, então ele ganha 500 de bonus
# se as vendas forem entre 5000 e 15000, então ele ganha 100 de bonus
# se as vendas forem menores do que 5000 então ele não ganha bonus

# vendas = 17000

# if vendas >= 15000:
#     bonus = 500
# else:
#     if vendas >= 5000:
#         bonus = 100
#     else:
#         bonus = 0

# print(f"Bonus do funcionário: {bonus}")

# if vendas >= 15000:
#     bonus = 500
# elif vendas >= 5000:
#     bonus = 100
# else:
#     bonus = 0

# print(f"Bonus do funcionário: {bonus}")


# Exemplo 3:
# bonus dos funcionários
# vendas maiores do que 15000, então ele ganha 500 de bonus
# se as vendas forem entre 5000 e 15000, então ele ganha 100 de bonus
# se as vendas forem menores do que 5000 então ele não ganha bonus
# Só ganha bonus se as vendas totais da empresa forem maiores do que 100000

# vendas_empresa = 200_000
# meta_empresa = 100_000
# vendas_funcionario = 16000

# if vendas_funcionario >= 15000 and vendas_empresa >= meta_empresa:
#     bonus = 500
# elif vendas_funcionario >= 5000 and vendas_empresa >= meta_empresa:
#     bonus = 100
# else:
#     bonus = 0

# print(f"Bonus do funcionário: {bonus}")
