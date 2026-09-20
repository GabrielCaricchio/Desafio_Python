# 1
print("####### Exercicio 1:")
fat = 45000
custo = 23500
lucro = fat - custo
margem = lucro / fat

print(f"Lucro: R${lucro:,.2f}, Margem: {margem:.0%}")

# 2
print("####### Exercício 2")
nome = " mArCoS aNtOnIo rOcHa "
email = " MARCOS.ROCHA@GMAIL.COM "

nome = nome.strip().title()
print(nome)

email = email.strip()
email = email.lower()
print(email)

# 3
print("####### Exercicio 3:")
email = "andre_silva@empresa.com.br"
novo_dominio = "@grupocorp.com"

# posicao_a = email.find("@")
# print(posicao_a)

# email = email[:posicao_a] + novo_dominio
# print(email)

email = email.replace("@empresa.com.br", "@grupocorp.com")
print(email)

# 4 
print("####### Exercicio 4:")
email = "beatriz.oliveira@grupocorp.com"

posicao_a = email.find("@")

username = email[:posicao_a]
print(username)

# 5
print("####### Exercicio 5:")
mensagem = "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"
nome = "lucas ferreira souza"
posicao_espaco = nome.find(" ")
pri_nome = nome[:posicao_espaco].capitalize()

mensagem = mensagem.replace("[Primeiro Nome]", pri_nome)
print(mensagem)