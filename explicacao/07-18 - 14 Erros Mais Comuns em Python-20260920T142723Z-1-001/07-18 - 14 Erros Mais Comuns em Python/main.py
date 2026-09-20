# Python - Erros mais comuns e Tipos de erros no Python

# Syntax Error
populacao = {"Rio de Janeiro" 6000000,
            "São Paulo": 12000000}
print(populacao["Rio de Janeiro"])

# Indentation Error
cidade = "Rio de Janeiro"
if populacao[cidade] > 1000000:
print("Cidade Grande")

# NameError
print(estado)

# KeyError
print(populacao["Brasília"])
# lembre do get

# IndexError
cidades = ["Rio de Janeiro", "São Paulo"]
print(cidades[3])

# TypeError
preco = "R$5,50"
quantidade = 2
mensagem = "Venda de " + quantidade + " produtos saindo a " + preco + " cada"

# ValueError
preco = float(preco)
valor_compra = preco * quantidade 
print(valor_compra)

# ZeroDivisionError
bonus_loja = 1000
vendas = [100, 200, 300, 290, 110, 340, 320, 330, 345]
meta = 350
qtde_bateram_meta = 0
for venda in vendas:
    if venda > meta:
        qtde_bateram_meta += 1

print("Bonus por vendedor:", bonus_loja / qtde_bateram_meta)

# ModuleNotFoundError
import pandas as pd
base = pd.read_csv("base.csv")
print(base)

# FileNotFoundError
base_copia = pd.read_csv("base")
base2 = pd.read_csv("base2.csv")

# PermissionError
base2.to_csv("base.csv")

# UnicodeError
with open("texto.txt", "r", encoding="ascii") as arquivo:
    texto = arquivo.read()
    print(texto)

# AttributeError
print(vendas.get(0))

# UnboundLocalError
def calcular_imposto(valor):
    imposto = valor * taxa
    taxa = 0.15
    print(imposto)

calcular_imposto(1500)