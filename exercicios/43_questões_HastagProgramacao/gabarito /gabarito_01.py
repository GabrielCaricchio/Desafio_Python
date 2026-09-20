# 1
print("####### Exercicio 1:")
fat = 50000
perc_bonus = 0.1
bonus_total = fat * perc_bonus
fat_liquido = fat - bonus_total
print("Fat Liquido", fat_liquido)
print("Bonus Total", bonus_total)

# 2 
print("####### Exercicio 2:")
estoque = 250
vendas = 78
reposicao = 100

estoque = estoque - vendas + reposicao
print("Estoque Final", estoque)

# 3 
print("####### Exercicio 3:")
caixas = 1250
capacidade_caminhao = 12

caminhoes_completos = caixas // capacidade_caminhao
print("Caminhoes Completos", caminhoes_completos)

caixas_restantes = caixas % capacidade_caminhao
print("Caixas Restantes", caixas_restantes)

# 4
print("####### Exercicio 4:")
fat = 15000
custos = 5000
perc_imposto = 0.15

imposto = fat * perc_imposto
lucro = fat - custos - imposto
margem = lucro / fat
print("Faturamento", fat)
print("Lucro", lucro)
print("Margem", margem)

meta_atingida = margem > 0.3
print("Meta Atingida?", meta_atingida)

# 5
print("####### Exercicio 5:")
duracao = 40
anos = 40 // 12
meses_sobram = 40 % 12
print("Duração do contrato é de", anos, "anos e", meses_sobram, "meses")