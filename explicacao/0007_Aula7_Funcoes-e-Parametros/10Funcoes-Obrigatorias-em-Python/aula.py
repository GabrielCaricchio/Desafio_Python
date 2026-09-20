# função 1
# print

# produto = "iphone"
# quantidade_estoque = 200

# print("O produto", produto, "tem", quantidade_estoque, "unidades no estoque", sep=";")


# import time
# print("Contagem")
# for i in range(5):
#     # print(5 - i, end="\n")
#     print(5 - i, end="\r")
#     time.sleep(1)
# print("Acabou")

# função 2
# help
# help(print)

# def calcular_imposto(faturamento, taxa):
#     """
#     faturamento (float): o faturamento da empresa que vamos calcular o imposto
#     taxa (float): a taxa percentual de imposto sobre o faturamento (ex: 0.2)

#     returns: imposto, faturamento_liquido
#     imposto (float):  valor total do imposto calculado sobre o faturamento
#     faturamento_liquido (float): quanto sobrou do faturamento depois de descontado o imposto
#     """
#     imposto = faturamento * taxa
#     return imposto, faturamento - imposto

# help(calcular_imposto)

# função 3
# range

# lista = list(range(5))
# lista = list(range(1, 6))
# lista = list(range(1, 10, 2))
# lista = list(range(5, 0, -1))

# print(lista)

# import time
# for i in range(5, 0, -1):
#     print(i, end="\r")
#     time.sleep(1)

# função 4
# map

# salarios = [1000, 5000, 7000, 850]

# def aumentar_salario(salario):
#     if salario > 3000:
#         novo_salario = salario * 1.08
#     else:
#         novo_salario = salario * 1.1
#     return novo_salario

# # novos_salarios = list(map(aumentar_salario, salarios))
# novos_salarios = list(map(lambda x: x * 1.1, salarios))
# print(novos_salarios)
    
# função 5
# filter
# salarios = [1000, 5000, 7000, 850]

# salarios_altos = list(filter(lambda x: x > 2000, salarios))
# print(salarios_altos)

# função 6
# sum
# custos = [600, 5000, 350, 4000]

# # custo_total = sum(custos)
# custo_total = sum(custos, start=1000)
# print(custo_total)

# função 7
# sorted
# salarios = [1000, 5000, 7000, 850]
# salarios_ordenados = sorted(salarios, reverse=True)
# print(salarios_ordenados)

# salarios = [
#     (1000, 500, 180),
#     (5000, 40, 200),
#     (7000, 0, 0),
#     (600, 4000, 150)
# ]
# funcionarios_ordenados = sorted(salarios, reverse=True, key=lambda x: sum(x))
# print(funcionarios_ordenados)

# função 8
# enumerate
# salarios = [1000, 5000, 7000, 850]
# funcionarios = ["lira", "alon", "amanda", "marcus"]

# for salario in salarios:
#     print(salario)

# for i, salario in enumerate(salarios):
#     funcionario = funcionarios[i]
#     print("Novo salário do",funcionario, "é", salario * 1.1)

# função 9
# zip

# for funcionario, salario in zip(funcionarios, salarios):
#     print("Novo salário do",funcionario, "é", salario * 1.1)

# dic_salarios = dict(zip(funcionarios, salarios)) 
# print(dic_salarios)

# função 10
# open

# arquivo = open("salarios_funcionarios.txt", "a", encoding="utf-8")

# for funcionario, salario in zip(funcionarios, salarios):
#     arquivo.write(f"Novo salário do {funcionario} é {salario * 1.1}\n")
# arquivo.close()

# arquivo = open("salarios_funcionarios.txt", "r", encoding="utf-8")
# texto = arquivo.read()
# print("Texto do arquivo:")
# print(texto)
# arquivo.close()

# with open("salarios_funcionarios.txt", "r", encoding="utf-8") as arquivo:
#     texto = arquivo.read()
# print("Texto do arquivo:")
# print(texto)