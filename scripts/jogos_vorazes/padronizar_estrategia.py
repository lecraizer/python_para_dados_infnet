import os
import re

pasta = "caminho/para/sua/pasta"

for arquivo in os.listdir(pasta):
    if arquivo.endswith(".py"):
        caminho_arquivo = os.path.join(pasta, arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()

        novo_conteudo = re.sub(
            r"def\s+estrategia\w*\s*\(",
            "def estrategia(",
            conteudo
        )

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(novo_conteudo)

print("Pronto!")
