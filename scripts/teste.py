def normalizar_texto(string):
    string = string.lower().strip()
    return string


frase = 'UMA nOVa abordAGEM NA AULA de PyThOn          '

texto_normalizado = normalizar_texto(frase)
print(texto_normalizado)