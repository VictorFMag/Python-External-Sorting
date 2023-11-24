import os

caminho_pasta = 'file_parts'

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
        caminho_completo = os.path.join("file_parts", arquivo)
        
        # Verifica se é um arquivo (e não uma subpasta)
        if os.path.isfile(caminho_completo):
            os.remove(caminho_completo)

#=======================================================================================================================

import heapsort as hs

def divide_arquivo(nome_arquivo, linhas_por_arquivo):
    if contar_arquivos_em_pasta(caminho_pasta) == 0:
        
        with open(nome_arquivo, 'r') as arquivo_origem:
            if not os.path.exists("file_parts/bigger_files"):
                os.makedirs("file_parts/bigger_files")
                print("Pasta criada com sucesso!")
            
            indice_arquivo = 0
            linha = arquivo_origem.readline()
            
            while linha:
                caminho_subpasta = os.path.join('file_parts', 'minor_files')
                if not os.path.exists(caminho_subpasta):
                    os.makedirs(caminho_subpasta)
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
        limpaPasta(caminho_pasta)
        divide_arquivo(nome_arquivo, linhas_por_arquivo)

#=======================================================================================================================

def merge_files(): # falta arrumar isso
    caminho_subpasta = os.path.join('file_parts', 'bigger_files')
    if not os.path.exists(caminho_subpasta):
        os.makedirs(caminho_subpasta)

    arquivos = os.listdir(caminho_pasta)
    partes_ordenadas = [sorted(arquivos[i:i+5]) for i in range(0, len(arquivos), 5)]

    for i, partes in enumerate(partes_ordenadas):
        with open(os.path.join(caminho_subpasta, f"arquivo_{i}_ordenado.txt"), "w") as arquivo_ordenado:
            for parte in partes:
                with open(os.path.join(caminho_pasta, parte), "r") as arquivo_parte:
                    arquivo_ordenado.write(arquivo_parte.read())

def achaMenor(*nums):
    menor = nums[0]
    for num in nums[1:]:
        if num < menor:
            menor = num
    return menor