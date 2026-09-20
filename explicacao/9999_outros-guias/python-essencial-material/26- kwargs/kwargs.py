def diz_ola(**nomes):
    print("Olá", end=" ")
    for valor in nomes.values():
        print(valor, end=" ")


diz_ola(primeiro_nome="Paulo", nome_meio="Raoni", ultimo_nome="Bezerra")
