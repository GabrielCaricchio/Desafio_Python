lista_vendas = [100, 50, 1000, 800, 35]

print(lista_vendas[0]) # pegar um item da lista

# tamanho da lista
qtde_vendas = len(lista_vendas) 
print(qtde_vendas)

# somar todos os itens
total_vendas = sum(lista_vendas)
print(total_vendas)

# max, min, media
print(max(lista_vendas))
print(min(lista_vendas))
print(total_vendas / qtde_vendas)

# encontrar um elemento (a posicao do elemento)
lista_produtos = ["iphone", "ipad", "apple watch", "airpod", "macbook"]
print("Airpod" in lista_produtos)

posicao = lista_produtos.index("airpod")
print(posicao)

pedaco_lista = lista_produtos[posicao:]
print(pedaco_lista)

# edita um item
lista_precos = [5000, 7000, 3000, 1000, 10000]
novo_preco = lista_precos[0] * 1.1
lista_precos[0] = novo_preco
print(lista_precos)

# remover um item da lista
lista_produtos.remove("macbook")
# item_removido = lista_produtos.pop(-1)
print(lista_produtos)
# print(item_removido)

# adicionar um item na lista
lista_produtos.append("macbook")

lista2_produtos = ["PC", "air tag", "caixa de som"]
lista_produtos.extend(lista2_produtos)
print(lista_produtos)

# inserir um item em uma posição específica
lista_produtos.insert(1, "airpod")
print(lista_produtos)

# contar quantas vezes um item aparece na lista
print(lista_produtos.count("airpod"))

# ordenar uma lista
lista_precos.sort(reverse=True)
print(lista_precos)