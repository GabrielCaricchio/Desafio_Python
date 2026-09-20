lista_produtos = ["ipad", "iphone", "airpod"]
lista_precos = [7000, 5000, 2000]

dic_produtos = {"ipad": 7000, "iphone": 5000, "airpod": 2000}

# pegar um item
produto = "iphone"
posicao = lista_produtos.index(produto)
preco = lista_precos[posicao]
print(produto, preco)

print(dic_produtos["ipad"])

dic_vendas = {"lira": [1000, 500, 1500], "joao": [500, 400, 500]}
print(dic_vendas["lira"])

# adicionar um item
# editar um item
dic_produtos["iphone"] = dic_produtos["iphone"] * 1.1

dic_produtos["macbook"] = 12000
print(dic_produtos)

# remover um item
item_removido = dic_produtos.pop("macbook")
print(dic_produtos)
print(item_removido)

# verificar se existe um item no dicionário
print("iphone" in dic_produtos)
print("iphone" in dic_produtos.keys())
print(2000 in dic_produtos.values())

produtos = list(dic_produtos.keys())
print(produtos)
precos = list(dic_produtos.values())
print(precos)


# contagem de itens no dicionários
qtde = len(dic_produtos)
print(qtde)


dic_produtos = {"ipad": 7000, "iphone": 5000, "airpod": 2000, "macbook": 12000}

produto_buscado = input("Digite o nome do produto:")
produto_buscado = produto_buscado.strip()
produto_buscado = produto_buscado.lower()

if produto_buscado in dic_produtos:
    preco = dic_produtos[produto_buscado]
    print("Produto encontrado")
    print(f"Produto: {produto_buscado}, Preço: R${preco}")
else:
    print("Produto não encontrado")

