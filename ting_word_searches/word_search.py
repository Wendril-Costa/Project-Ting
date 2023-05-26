def exists_word(word, instance):
    results = []
    for file in map(instance.search, range(len(instance))):
        occurrences = []
        for index, line in enumerate(file['linhas_do_arquivo'], start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": index})
        if occurrences:
            result = {
                "palavra": word,
                "arquivo": file['nome_do_arquivo'],
                "ocorrencias": occurrences
            }
            results.append(result)
    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
