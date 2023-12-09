import os

def contar_arquivos_em_pasta(caminho_pasta):
    if os.path.exists(caminho_pasta) and os.path.isdir(caminho_pasta):
        return len([nome for nome in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, nome))])
    return 0

def limpaPasta(caminho_pasta):
    for arquivo in os.listdir(caminho_pasta):
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        if os.path.isfile(caminho_completo):
            os.remove(caminho_completo)

def criaPasta(caminho_pasta):
    if os.path.exists(caminho_pasta):
        limpaPasta(caminho_pasta)
    else:
        os.makedirs(caminho_pasta)
