from string import Template


def get_template(arquivo):
    with open(arquivo, mode='r', encoding='utf-8') as arq:
        template_arquivo = arq.read()
    return Template(template_arquivo)
