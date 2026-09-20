# Controles de Loop (break, continue e pass) são mudanças na execução normal de um loop

# break = usado para finalizar um loop
# continue = pula para a próxima iteração do loop
# pass = não faz nada, apenas age como um place holder

while True:
    alguma_coisa = input("Digite alguma coisa: ")
    if alguma_coisa != "":
        break

numero_telefone = "+55 (21) 12345-6789"

for i in numero_telefone:
    if i == "+" or i == "(" or i == ")" or i == "-":
        continue
    print(i, end="")

for i in range(1, 11):
    if i == 5:
        pass
    else:
        print(i)