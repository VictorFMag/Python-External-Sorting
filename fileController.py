# Funções auxiliares
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
        
        # Verifica se é um arquivo (e não uma subpasta)
        if os.path.isfile(caminho_completo):
            os.remove(caminho_completo)

#=======================================================================================================================

import heapsort as hs

def divide_arquivo(nome_arquivo, linhas_por_arquivo):
    if contar_arquivos_em_pasta("file_parts/minor_files") == 0:
        
        with open(nome_arquivo, 'r') as arquivo_origem:
            indice_arquivo = 0
            linha = arquivo_origem.readline()
            
            while linha:
                caminho_subpasta = os.path.join('file_parts', 'minor_files')
                if not os.path.exists(caminho_subpasta):
                    os.makedirs(caminho_subpasta)
                    print("Pasta minor_files criada com sucesso!")
                nome_parte = os.path.join(caminho_subpasta, f'parte_{indice_arquivo}.txt') # Cria os arquivos dentro da pasta
                
                with open(nome_parte, 'w') as parte_arquivo:
                    contador_linhas = 0
                    auxArr = []
                    
                    while contador_linhas < linhas_por_arquivo and linha:
                        auxArr.append(linha)
                        linha = arquivo_origem.readline()
                        contador_linhas += 1
                    
                    hs.heap_sort(auxArr)  # Ordena as linhas com Heap Sort, garantindo que o tempo de ordenação seja parecido para todos os tamanhos de memória
                    parte_arquivo.write("".join(auxArr))

                indice_arquivo += 1
        print(f'{indice_arquivo} partes criadas.')
    
    else:
        limpaPasta('file_parts/minor_files')
        divide_arquivo(nome_arquivo, linhas_por_arquivo)

#=======================================================================================================================

def merge_files(arquivos_por_merge):
    caminho_subpasta = os.path.join('file_parts', 'medium_files')
    if not os.path.exists(caminho_subpasta):
        os.makedirs(caminho_subpasta)
        print("Pasta medium_files criada com sucesso!")
    else:
        limpaPasta(caminho_subpasta)

    #

    for i in range(0, contar_arquivos_em_pasta('file_parts/minor_parts')+1, 5):
        arrOfLines = []
        arrOfArquives = []
        for j in range(arquivos_por_merge):
            with open(f'file_parts/minor_files/parte_{j}.txt', 'r') as file:
                linhas = file.readlines()
                arrOfLines.append(linhas[0])
                novoArquivo = Arquivo(0, j)
                arrOfArquives.append(novoArquivo)

        cont = 0
        nome_arquivo_medio = os.path.join(caminho_subpasta, f'parte_media_{cont}.txt') # Cria os arquivos dentro da pasta
        with open(nome_arquivo_medio, 'w') as arquivo_medio:
            for j in range(len(arrOfLines)):
                menor = min(arrOfLines)
                arquivo_medio.write(menor)
                idxArquivoComMenor = arrOfLines.index(menor)
                
                linha = Arquivo.avancarPointer(Arquivo.encontrar_por_id(arrOfArquives, idxArquivoComMenor))
                #arrOfLines[idxArquivoComMenor] = 
        cont+=1

class Arquivo:
    def __init__(self, arquivo_id, ultima_linha_analisada):
        self.id = arquivo_id
        self.ultimaLinhaAnalisada = ultima_linha_analisada
    
    def encontrar_por_id(arrOfArquives, arquivo_id):
        for arquivo in arrOfArquives:
            if arquivo.id == arquivo_id:
                return arquivo
        return None  # Retorna None se não encontrar o arquivo com o ID especificado
    
    def avancarPointer(arquivo_id):
        arquivo_id.ultimaLinhaAnalisada += 1