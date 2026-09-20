
import os

path_to_file = "D:/temp/teste"

if os.path.exists(path_to_file):
    print("Essa localização existe")
    if os.path.isfile(path_to_file):
        print("É um arquivo")
    elif os.path.isdir(path_to_file):
        print("É um diretório")
else:
    print("Esse local não existe")