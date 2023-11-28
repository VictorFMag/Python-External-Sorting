# Funções menoriliares
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
                    menorArr = []
                    
                    while contador_linhas < linhas_por_arquivo and linha:
                        menorArr.append(linha)
                        linha = arquivo_origem.readline()
                        contador_linhas += 1
                    
                    hs.heap_sort(menorArr)  # Ordena as linhas com Heap Sort, garantindo que o tempo de ordenação seja parecido para todos os tamanhos de memória
                    parte_arquivo.write("".join(menorArr))

                indice_arquivo += 1
        print(f'{indice_arquivo} partes criadas.')
    
    else:
        limpaPasta('file_parts/minor_files')
        divide_arquivo(nome_arquivo, linhas_por_arquivo)

#=======================================================================================================================

def merge_files(arquivos_por_merge):
    contadorArquivos =0
    caminho_subpasta = os.path.join('file_parts', 'medium_files')
    if not os.path.exists(caminho_subpasta):
        os.makedirs(caminho_subpasta)
        print("Pasta medium_files criada com sucesso!")
    else:
        limpaPasta(caminho_subpasta)

    num_arquivos = contar_arquivos_em_pasta('file_parts/minor_files')

    # Iterar sobre os arquivos ordenados em grupos de 'arquivos_por_merge'
    for i in range(0, num_arquivos, arquivos_por_merge):
        print("Faixa analisada:", i, "até", i + arquivos_por_merge - 1)

        # Lista para armazenar os arquivos a serem mesclados nesta iteração
        files_to_merge = []
        for j in range(arquivos_por_merge):
            file_number = i + j
            file_path = f'file_parts/minor_files/parte_{file_number}.txt'
            if os.path.exists(file_path):
                files_to_merge.append(open(file_path, 'r'))

        output_file_path = os.path.join(caminho_subpasta, f'parte_media_{i}.txt')

        contadorArquivos+=1

        with open(output_file_path, 'w') as output_file:
            merged_lines = []

            # Ler a primeira linha de cada arquivo e armazenar em uma lista
            for file in files_to_merge:
                line = file.readline()
                if line:
                    merged_lines.append((line, file))

            while merged_lines:
                # Encontrar a menor linha entre as linhas lidas dos arquivos
                merged_lines.sort(key=lambda x: x[0])
                smallest_line, smallest_file = merged_lines.pop(0)

                # Escrever a menor linha no arquivo de saída
                output_file.write(smallest_line)

                # Ler a próxima linha do arquivo que teve a menor linha escrita
                next_line = smallest_file.readline()
                if next_line:
                    merged_lines.append((next_line, smallest_file))

        # Fechar todos os arquivos abertos
        for file in files_to_merge:
            file.close()
    print(contadorArquivos,"arquivos criados")
