
import shutil
import os

path = "pasta_com_conteudo"

try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path)
except PermissionError:
    print("Você não tem permissão para deletar essa pasta.")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except OSError:
    print("Você não tem permissão para deletar usando esse método.")
else:
    print(path + " foi deletada")