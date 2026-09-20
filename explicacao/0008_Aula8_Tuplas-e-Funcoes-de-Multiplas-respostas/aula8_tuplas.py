# bonus 1: R$2 por venda feita
# bonus 2: 1% do valor de vendas

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)
    return bonus1, bonus2


vendas = [100, 250, 400, 1000]
# unpacking da tupla
bonus1, bonus2 = calcular_bonus(vendas)

print(bonus1)
print(bonus2)

# lista_telas = [(1090, 1080), (2140, 1080)]
# for altura, largura in lista_telas:
#     print(altura, largura)


# bonus 1: R$2 por venda feita
# bonus 2: 1% do valor de vendas

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)
    return bonus1, bonus2

vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

# bonus de cada funcionario
# total de bonus 1 pago aos funcionários
# total de bonus 2 pago aos funcionários


total_bonus1 = 0
total_bonus2 = 0
for vendedor in vendas:
    bonus1, bonus2 = calcular_bonus(vendas[vendedor])
    print(f"Vendedor: {vendedor}. Bonus1: {bonus1}. Bonus2: {bonus2}")
    total_bonus1 = total_bonus1 + bonus1
    total_bonus2 = total_bonus2 + bonus2

print("Total Bonus1:", total_bonus1)
print("Total Bonus2:", total_bonus2)
print("Total Bonus Geral:", total_bonus1 + total_bonus2)