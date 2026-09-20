# 1
print("####### Exercicio 1:")
coordenadas = (-23.5505, -46.6333)
latitude, longitude = coordenadas

print(f"Iniciando entrega. Latitude: {latitude}, Longitude: {longitude}")

# 2
print("####### Exercicio 2:")

def calcular_folha(salario):
    perc_desconto = 0.1
    desconto = perc_desconto * salario
    salario_liquido = salario - desconto
    return desconto, salario_liquido

salario = 5000
desconto_salarial, salario_liq = calcular_folha(salario)
print(f"Desconto: R${desconto_salarial} | Salário Líquido: R${salario_liq}")

# 3
print("####### Exercicio 3:")

# (produto, preco_unitario, quantidade)
vendas_dia = [("Monitor", 900, 2), ("Teclado", 150, 5), ("Mouse", 80, 10)]

for produto, preco, qtde in vendas_dia:
    print(f"Produto: {produto} | Total: R${preco * qtde}")

# 4 
print("####### Exercicio 4:")

def analisar_vendas(lista_vendas):
    total_vendas = sum(lista_vendas)
    media_vendas = total_vendas / len(lista_vendas)
    return total_vendas, media_vendas

dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}

for filial in dados_filiais:
    vendas_filial = dados_filiais[filial]
    total_vendas_filial, media_vendas_filial = analisar_vendas(vendas_filial)
    print(f"Filial {filial} -> Total: R${total_vendas_filial}, Média: R${media_vendas_filial}")

# 5
print("####### Exercicio 5:")

def resumo_chamados(lista_tempos_chamados):
    qtde_chamados = len(lista_tempos_chamados)
    tempo_maximo = max(lista_tempos_chamados)
    return qtde_chamados, tempo_maximo

tempos = [15, 45, 10, 120, 30]
qtde, tempo_maximo = resumo_chamados(tempos)

print(f"Foram abertos {qtde} chamados hoje. Tempo Máximo de SLA: {tempo_maximo} minutos")