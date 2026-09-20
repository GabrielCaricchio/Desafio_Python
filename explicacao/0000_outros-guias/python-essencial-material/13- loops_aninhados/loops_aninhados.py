# loops aninhados = loops dentro de outros loops

# sendo que os loops de dentro terminam todas as suas iterações 
# para então o loop de fora terminar uma iteração

####
####
####

linhas = int( input("Quantas linhas?") )
colunas = int( input("Quantas colunas?") )
caractere = input("Informe o caractere a ser usado: ")

for i in range(linhas):
    for j in range(colunas):
        print(caractere, end="")
    print()

