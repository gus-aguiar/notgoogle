def exists_word(word, instance):
    linhas = []
    for i in range(len(instance)):
        for j in range(len(instance.search(i)["linhas_do_arquivo"])):
            if (
                word.lower()
                in instance.search(i)["linhas_do_arquivo"][j].lower()
            ):
                linhas.append({"linha": j + 1})
    dict = {
        "palavra": word,
        "arquivo": instance.search(i)["nome_do_arquivo"],
        "ocorrencias": linhas,
    }
    return [dict] if len(linhas) > 0 else []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
