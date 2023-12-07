import os

def contar_arquivos_em_pasta(caminho_pasta):
    if os.path.exists(caminho_pasta) and os.path.isdir(caminho_pasta):
        lista_arquivos = os.listdir(caminho_pasta)
        quantidade_arquivos = 0
        
        for arquivo in lista_arquivos:
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            
            # Verifica se é um arquivo e não uma subpasta
            if os.path.isfile(caminho_arquivo):
                quantidade_arquivos += 1
        
        return quantidade_arquivos
    else:
        return 0  # Retorna 0 se o caminho não existir ou não for um diretório
    
def limpaPasta(caminho_pasta):
    # Lista todos os arquivos na pasta
    arquivos = os.listdir(caminho_pasta)
    
    # Loop para apagar cada arquivo na pasta
    for arquivo in arquivos:
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        
        # Verifica se é um arquivo e não uma subpasta
        if os.path.isfile(caminho_completo):
            os.remove(caminho_completo)

def criaPasta(caminho_pasta):
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
    else:
        limpaPasta(caminho_pasta)
