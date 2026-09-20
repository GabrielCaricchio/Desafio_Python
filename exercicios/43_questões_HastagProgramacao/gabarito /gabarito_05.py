# 1
# print("####### Exercicio 1:")
# valor = input("Digite o valor que você vai querer investir:")
# valor = valor.replace("R$", "").replace(".", "").replace(",", ".")
# valor = float(valor)

# if valor < 1000:
#     print("Perfil iniciante: Sugerimos Tesouro Direto")
# elif valor <= 5000:
#     print("Perfil moderado: Sugerimos Fundos Imobiliários")
# else:
#     print("Perfil arrojado: Sugerimos Ações")

# 2
# print("####### Exercicio 2:")
# admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"]

# email = input("Digite seu e-mail:")
# email = email.strip().lower()

# if email in admins:
#     print("Acesso liberado! Bem-vindo ao painel de controle")
# else:
#     print("Acesso negado. Você não tem permissões de administrador")

# 3
print("####### Exercicio 3:")
valor_carrinho = 400

if valor_carrinho < 200:
    perc_desconto = 0
elif valor_carrinho < 500:
    perc_desconto = 0.1
else:
    perc_desconto = 0.15

desconto = valor_carrinho * perc_desconto
valor_final = valor_carrinho - desconto
print(f"Desconto: R${desconto:,.2f}. Valor Total: R${valor_final:,.2f}")

# 4
print("####### Exercicio 4:")
meta = 1000
vendas_vendedor = 1000

meta_loja = 5000
vendas_loja = 4000

if vendas_loja >= meta_loja and vendas_vendedor >= meta:
    bonus = 0.2 * vendas_vendedor
else:
    bonus = 0

print(f"Seu bônus este mês é de: R${bonus:.2f}")

# 5
assunto = "Problemas com acesso"

assunto = assunto.lower()

if "pagamento" in assunto or "boleto" in assunto:
    print("Encaminhado para o Financeiro")
elif "entrega" in assunto or "atraso" in assunto:
    print("Encaminhado para a Logística")
else:
    print("Encaminhado para o Suporte Geral")

    
