def find_occurrences(word, lines):
    return [
        {"linha": index + 1}
        for index, line in enumerate(lines)
        if word.lower() in line.lower()
    ]


def exists_word(word, instance):
    return [
        {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": find_occurrences(word, file["linhas_do_arquivo"]),
        }
        for file in map(instance.search, range(len(instance)))
        if find_occurrences(word, file["linhas_do_arquivo"])
    ]


def search_by_word(word, instance):
    return [
        {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": index + 1, "conteudo": line}
                for index, line in enumerate(file["linhas_do_arquivo"])
                if word.lower() in line.lower()
            ],
        }
        for file in map(instance.search, range(len(instance)))
        if find_occurrences(word, file["linhas_do_arquivo"])
    ]
