import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file in [item["nome_do_arquivo"] for item in instance.items]:
        print(
            f"Arquivo {path_file} já foi processado anteriormente",
            file=sys.stdout,
        )
        return

    lines = txt_importer(path_file)

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(file_info)

    print(file_info, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return

    try:
        removed_file = instance.dequeue()
        print(
            f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout,
        )
    except IndexError:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        file_info = instance.search(position)
        print(file_info, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
