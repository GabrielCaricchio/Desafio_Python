import os

origem = "origem/teste.tx"
destino = "destino/alguma_coisaa.txt"

try:
    if os.path.exists(destino):
        print("Já existe um arquivo lá")
    else:
        os.replace(origem, destino)
        print(origem + " foi movido para o destino")
except FileNotFoundError:
    print(destino + " não foi encontrado")