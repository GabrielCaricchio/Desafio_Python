# 1
print("####### Exercicio 1:")
vendas = [1500, 2000, 800, 3500, 1200]

total_vendas = sum(vendas)
qtde_dias = len(vendas)
media_vendas = total_vendas / qtde_dias

maior_venda = max(vendas)
menor_venda = min(vendas)
print(f"Total: {total_vendas}, Média de Vendas: {media_vendas}, Maior Venda: {maior_venda}, Menor Venda: {menor_venda}")


# 2
print("####### Exercicio 2:")
estoque = ["monitor", "teclado", "mouse", "headset"]
estoque.append("webcam")
posicao_teclado = estoque.index("teclado")
estoque[posicao_teclado] = "teclado mecânico"

impressora_no_estoque = "impressora" in estoque
print("Impressora no estoque?", impressora_no_estoque)

estoque.remove("mouse")
print(estoque)

# 3
print("####### Exercicio 3:")
fretes = [50, 80, 20, 150, 40]
fretes.sort(reverse=True)
print(fretes)
top_fretes = fretes[:2]
print(top_fretes)

# 4
print("####### Exercicio 4:")
rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidades = ["Itu", "Valinhos"]

rota.extend(novas_cidades)
print(rota)
posicao_sorocaba = rota.index("Sorocaba") + 1
print(f"Sorocaba é a {posicao_sorocaba}ª cidade da rota")

# 5
precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto", "Champagne"]

vinho_escolhido = input("Digite o vinho a ser alterado:")
novo_preco = input("Novo Preço:")
novo_preco = novo_preco.replace("R$", "").replace(".", "").replace(",", ".")
novo_preco = float(novo_preco)

posicao_vinho = vinhos.index(vinho_escolhido)
precos[posicao_vinho] = novo_preco
print(vinhos)
print(precos)