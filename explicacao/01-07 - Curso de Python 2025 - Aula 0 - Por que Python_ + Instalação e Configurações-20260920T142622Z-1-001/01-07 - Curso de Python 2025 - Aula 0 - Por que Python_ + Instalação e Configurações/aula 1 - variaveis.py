faturamento = 1100 # numero inteiro
custo = 600


print("Faturamento", faturamento)
novas_vendas = 1000

faturamento = faturamento + novas_vendas

imposto = 0.15 * faturamento # float
print(imposto)
lucro = faturamento - custo - imposto

print("Faturamento", faturamento)
print("Custo", custo)
print("Lucro", lucro)

mensagem = "O faturamento da loja foi de 2100" # string
teve_lucro = True # boolean

margem_lucro = lucro / faturamento
print("Margem", margem_lucro)

# int = numeros inteiros
# float = numeros casa decimal
# strings = textos
# boolean = booleanos (True False)

# operadores especiais

# mod -> %
# resto da divisão de um número pelo outro
# 10 % 3

anos = int(310 / 12)
print(anos, "anos")

meses = 310 % 12
print(meses, "meses")

# floor division -> //
print(310 // 12)
