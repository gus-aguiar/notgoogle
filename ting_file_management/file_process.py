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
    sys.stdout.write(
        f"Arquivo {instance.search(0)['nome_do_arquivo']} removido com sucesso\n"
    )
    instance.dequeue()
    pass


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    pass
