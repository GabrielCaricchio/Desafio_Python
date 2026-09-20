# yield

def ler_csv(nome_arquivo):
    yield from open(nome_arquivo, "r")

vendas = ler_csv("vendas.csv")

for venda in vendas:
    print(venda)
