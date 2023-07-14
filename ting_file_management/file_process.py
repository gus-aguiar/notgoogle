from ting_file_management.file_management import txt_importer
import sys

# import os


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            sys.stdout.write("Arquivo já importado\n")
            return None
    f = txt_importer(path_file)
    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(f),
        "linhas_do_arquivo": f,
    }
    instance.enqueue(dict)
    sys.stdout.write(f"{dict}\n")
    return dict


def remove(instance):
    if instance.is_empty():
        sys.stdout.write("Não há elementos\n")
        return None
    instance_name = instance.search(0)["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {instance_name} removido com sucesso\n")
    instance.dequeue()


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        sys.stderr.write("Posição inválida\n")
        return None
    meta = instance.search(position)
    sys.stdout.write(f"{meta}\n")
