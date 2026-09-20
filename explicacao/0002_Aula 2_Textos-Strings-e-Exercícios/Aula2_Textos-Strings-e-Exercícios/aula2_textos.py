faturamento = 1000
custo = 600

lucro = faturamento - custo
# texto = "O lucro foi de " + str(lucro) + " e o faturamento foi de " + str(faturamento)
texto = f"O lucro foi de R${lucro} e o faturamento foi de R${faturamento}"
print(texto)

email = " EMAIL_FALSO@gmail.com "

email = email.lower() # colocar em letra minuscula
email = email.strip() # ajustar espaços vazios
print(email)

# tamanho
print(len(email))

# posicao
posicao = email.find("@")
print(posicao)

# pedaços do texto
servidor = email[posicao+1:]
print(servidor)

# email_falso@gmail.com

# trocar um pedaço do texto
novo_email = email.replace("gmail.com", "yahoo.com.br")
print(novo_email)

nome = "joão lira"
nome = nome.capitalize()
print(nome)
nome = nome.title()
print(nome)
nome = nome.upper()
print(nome)

# formatação numérica
faturamento = 1_000
custo = 600

lucro = faturamento - custo
margem = lucro / faturamento
# texto = "O lucro foi de " + str(lucro) + " e o faturamento foi de " + str(faturamento)
texto = f"O lucro foi de R${lucro:,.2f} e o faturamento foi de R${faturamento:,.2f} e a margem foi de {margem:.0%}"
print(texto)

# exercicio
nome = "joao paulo lira"
email = "emailfalsodolira@gmail.com"

# descubra o servidor do email
posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)

# descubra o 1º nome do usuario
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
primeiro_nome = primeiro_nome.capitalize()
print(primeiro_nome)


# criar uma mensagem personalizada dizendo "Usuario 1º nome foi cadastrado com sucesso no email tal"
mensagem = f"Usuario {primeiro_nome} foi cadastrado com sucesso no email {email}"
print(mensagem)