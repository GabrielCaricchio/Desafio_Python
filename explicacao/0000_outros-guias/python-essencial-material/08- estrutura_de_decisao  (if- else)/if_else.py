# Estruturas de Decisao sao blocos de código que executam caso uma dada condição seja verdadeira (True)
# Também são conhecidas como Estruturas de Condição.

idade = int(input("Digite sua idade: "))

if idade == 100:
    print("Um século de vida!")
elif idade >= 18:
    print("Maior de idade.")
elif idade >= 16 and idade <= 18: 
    print("Já pode votar.")
elif idade < 0:
    print("Você não nasceu ainda. =/")
elif idade >= 12:
    print("Você é um adolescente.")
else:
    print("Você é uma criança.")
