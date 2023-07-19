def exists_word(word, instance):
    result = []
    for i in range(len(instance)):
        dict = {
            "palavra": word,
            "arquivo": instance.search(i)["nome_do_arquivo"],
            "ocorrencias": aux_search(word, instance, i=i),
        }
        if len(dict["ocorrencias"]) > 0:
            result.append(dict)

    return result


def search_by_word(word, instance):
    result = []
    for i in range(len(instance)):
        dict = {
            "palavra": word,
            "arquivo": instance.search(i)["nome_do_arquivo"],
            "ocorrencias": aux_search(word, instance, type=True, i=i),
        }
        if len(dict["ocorrencias"]) > 0:
            result.append(dict)

    return result


def aux_search(word, instance, type=False, i=0):
    linhas_completo = []
    for j in range(len(instance.search(i)["linhas_do_arquivo"])):
        line = instance.search(i)["linhas_do_arquivo"][j]
        if word.lower() in line.lower():
            if type:
                linhas_completo.append({"linha": j + 1, "conteudo": line})
            else:
                linhas_completo.append({"linha": j + 1})
    return linhas_completo
