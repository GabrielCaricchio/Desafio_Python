# 1
print("####### Exercicio 1:")
for i in range(10):
    tempo_falta = 10 - i
    print(f"Faltam {tempo_falta} minutos para começar o treinamento")

# 2 
print("####### Exercicio 2:")
vendas = [2000, 5000, 1000, 8000, 3000]

comissao_total = 0
for venda in vendas:
    if venda > 4000:
        comissao = 0.1
    else:
        comissao = 0.05
    comissao_total = comissao_total + comissao * venda

print(f"Comissão total de R${comissao_total:,.2f}")

# 3
print("####### Exercicio 3:")
estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"]
estoque_quantidades = [5, 12, 2, 8, 15]

for i, quantidade in enumerate(estoque_quantidades):
    if quantidade < 8:
        produto = estoque_produtos[i]
        print(f"ALERTA: O produto {produto} está com apenas {quantidade} unidades no estoque!")

# 4
print("####### Exercicio 4:")
metas = {"jan": 1000, "fev": 1200, "mar": 1100}
gastos = {"jan": 900, "fev": 1350, "mar": 1100}

for mes in gastos:
    if gastos[mes] > metas[mes]:
        diferenca = gastos[mes] - metas[mes]
        print(f"Mês {mes}: Orçamento estourado em R${diferenca}.")
    else:
        print(f"Mês {mes}: Dentro do orçamento.")

# 5
print("####### Exercicio 5:")
precos = {"celular": 1500, "tablet": 2500, "notebook": 5000}
perc_aumento = input("Qual o aumento planejado?") # 10%
perc_aumento = perc_aumento.replace("%", "") # 10
perc_aumento = float(perc_aumento) / 100 # 0.1

for produto in precos:
    precos[produto] = precos[produto] * (1 + perc_aumento)

print(precos)