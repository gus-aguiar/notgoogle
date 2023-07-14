import os
import sys


def txt_importer(path_file):
    if not str(path_file).endswith(".txt"):
        return sys.stderr.write("Formato inválido")

    elif not os.path.exists(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    else:
        f = open(path_file, "r")
        data = f.read().split("\n")
        f.close()
        return data
