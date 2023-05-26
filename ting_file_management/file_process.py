import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    # Verifica se o arquivo já foi processado anteriormente
    if path_file in [item["nome_do_arquivo"] for item in instance.items]:
        print(
            f"Arquivo {path_file} já foi processado anteriormente",
            file=sys.stdout,
        )
        return

    # Importa o conteúdo do arquivo usando a função txt_importer
    lines = txt_importer(path_file)

    # Cria o dicionário com as informações do arquivo
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    # Adiciona o dicionário à fila
    instance.enqueue(file_info)

    # Mostra os dados processados via stdout
    print(file_info, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
