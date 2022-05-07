import os
import shutil
import re


def renomear_arquivos(pasta, inicio_numeracao):
    for root, dirs, files in os.walk(pasta):
        i = inicio_numeracao
        for file in files:
            if not re.search('\d{3}', file):
                file_name, file_ext = os.path.splitext(file)

                old_file_name = file_name + file_ext
                new_file_name = str(i).zfill(3) + '_' + file_name + file_ext

                new_file_name_completo = os.path.join(root, new_file_name)
                old_file_name_completo = os.path.join(root, old_file_name)

                shutil.move(old_file_name_completo, new_file_name_completo)
                i += 1
