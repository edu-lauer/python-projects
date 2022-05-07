import shutil


def zipar_arquivo(pasta, nome_pasta):
    shutil.make_archive(nome_pasta, 'zip', pasta)
