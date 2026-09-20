# 1
print("####### Exercicio 1:")

fat = input("Digite o faturamento:")
fat = fat.replace("R$", "").replace(".", "").replace(",", ".")
fat_numerico = float(fat)
perc_imposto = 0.15
imposto = fat_numerico * perc_imposto
print(f"Imposto pago: R${imposto:,.2f}")

# 2
print("####### Exercicio 2:")
mensagem = "Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail padronizado]"

nome = input("Digite o nome completo do colaborador:")
email = input("Digite o email do colaborador:")

nome = nome.strip()
email = email.strip().lower()

posicao_espaco = nome.find(" ")
pri_nome = nome[:posicao_espaco].capitalize()

mensagem = mensagem.replace("[Primeiro Nome]", pri_nome).replace("[E-mail padronizado]", email)
print(mensagem)

# 3
print("####### Exercicio 3:")
fat_lojaA = input("Faturamento da Loja A:")
fat_lojaB = input("Faturamento da Loja B:")

fat_lojaA = fat_lojaA.replace("R$", "").replace(".", "").replace(",", ".")
fat_lojaA = float(fat_lojaA)

fat_lojaB = fat_lojaB.replace("R$", "").replace(".", "").replace(",", ".")
fat_lojaB = float(fat_lojaB)

total_fat = fat_lojaA + fat_lojaB
media_fat = total_fat / 2

print(f"Faturamento Total: R${total_fat:,.2f}, Média de Faturamento: R${media_fat:,.2f}")