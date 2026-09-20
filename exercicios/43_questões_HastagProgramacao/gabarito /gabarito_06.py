# 1
print("####### Exercicio 1:")
clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}

nova_compra = 1500
clientes["Alon"] = clientes["Alon"] + nova_compra

clientes["Marcos"] = 2000
print(clientes)

# 2 
# print("####### Exercicio 2:")
# estoque = {"teclado": 50, "mouse": 120, "monitor": 30}
# produto = input("Digite o nome do produto:")

# produto = produto.strip().lower()

# if produto in estoque:
#     print(f"{produto} encontrado: {estoque[produto]} unidades no estoque")
# else:
#     print(f"{produto} não encontrado")

# 3
print("####### Exercicio 3:")
vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}

lista_vendas = list(vendas_regiao.values())
total_vendas = sum(lista_vendas)
qtde_vendas = len(lista_vendas)
media_vendas = total_vendas / qtde_vendas
print("Total Vendas", total_vendas)
print("Media de Vendas", media_vendas)

# 4
# print("####### Exercicio 4:")
# desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}
# nome = input("Digite o nome de um colaborador:")

# notas = desempenho[nome]
# print("Nome:", nome)
# print("Notas", notas)
# media_notas = sum(notas) / len(notas)
# print("Media", media_notas)

# 5
print("####### Exercicio 5:")
produtos = {"celular": 1500, "camera": 800, "radio": 200, "fone": 100}
item_removido = "celular"

produtos.pop(item_removido)
print(produtos)

celular_no_dic = "celular" in produtos
print("Celular no estoque?", celular_no_dic)