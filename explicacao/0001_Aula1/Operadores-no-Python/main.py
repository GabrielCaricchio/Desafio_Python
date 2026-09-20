# aritméticos (+, -, /, *, %, //)

faturamento = 400
custo = 150
lucro = faturamento - custo

print(lucro)

num1 = 10
num2 = 4

print(num1 // num2)

# assignement (atribuição) (=, +=, *=, :=)
i = 0
while i < 10:
    print("Se inscreve no canal")
    i += 1

print(qtde := 10)

# comparação (==, !=, >, <, >=, <=)
if not lucro > 500:
    print("Empresa pouco lucrativa")
else:
    print("Empresa muito lucrativa")

# lógicos (and, or, not)
if lucro > 500 or custo < 200:
    print("Excelente empresa")
else:
    print("Empresa normal")

# identidade (is)

faturamento = [1000]
custo = [1000]

if faturamento is custo:
    print("Não teve lucro")
else:
    print("Pode ter tido lucro ou prejuízo")

# membership (está dentro da "lista") -> in
vendedor = "João"
lista_vendedores = ["Lira", "João", "Amanda", "Larissa", "Alon"]

vendas = {
    "Lira": 1000,
    "Amanda": 2000,
    "João": 300
}

if vendedor in vendas:
    print(vendas[vendedor])
else:
    print("Vendedor não encontrado")
