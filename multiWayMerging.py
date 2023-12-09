import auxFunctions as AF
import os
import internalSortingMethods as sorter

#=======================================================================================================================

def divide_files(nome_arquivo, linhas_por_arquivo): # Divide o arquivo a ser ordenado em partes menores de acordo com a quantidade de linhas por arquivo definida em main.py
    if AF.contar_arquivos_em_pasta("file_parts/MultiWay/minor_files") == 0:
        
        with open(nome_arquivo, 'r') as arquivo_origem:
            indice_arquivo = 0
            linha = arquivo_origem.readline()
            
            while linha:
                caminho_subpasta = os.path.join('file_parts/MultiWay', 'minor_files')
                if not os.path.exists(caminho_subpasta):
                    os.makedirs(caminho_subpasta) # Não usei criaPasta() porque não quero que ela seja limpa caso já exista
                nome_parte = os.path.join(caminho_subpasta, f'part_{indice_arquivo}.txt')
                
                with open(nome_parte, 'w') as parte_arquivo:
                    contador_linhas = 0
                    menorArr = []
                    
                    while contador_linhas < linhas_por_arquivo and linha:
                        menorArr.append(linha)
                        linha = arquivo_origem.readline()
                        contador_linhas += 1
                    
                    sorter.heap_sort(menorArr)  # Ordena as linhas com Heap Sort, garantindo que o tempo de ordenação seja parecido para todos os tamanhos de memória
                    parte_arquivo.write("".join(menorArr))

                indice_arquivo += 1
        
        # Debugging
        print(f'{indice_arquivo} partes criadas.')
    
    else:
        AF.limpaPasta('file_parts/MultiWay/minor_files')
        divide_files(nome_arquivo, linhas_por_arquivo)

#=======================================================================================================================

def merge_files(arquivos_por_merge, contadorDeIteracoes, pasta_anterior):
    num_arquivos_pasta_anterior = AF.contar_arquivos_em_pasta(f'file_parts/MultiWay/{pasta_anterior}')
    
    if num_arquivos_pasta_anterior!=1:
        contadorArquivos = 0

        caminho_subpasta = os.path.join('file_parts/MultiWay', f'medium_files_{contadorDeIteracoes}')
        AF.criaPasta(caminho_subpasta)

        # Itera sobre os arquivos ordenados em lotes de 'arquivos_por_merge'
        for i in range(0, num_arquivos_pasta_anterior, arquivos_por_merge):

            # Debugging
            print("Faixa analisada:", i, "até", i + arquivos_por_merge - 1)

            # Lista para armazenar os arquivos a serem mesclados nesta iteração
            files_to_merge = []
            for j in range(arquivos_por_merge):
                file_number = i + j
                file_path = f'file_parts/MultiWay/{pasta_anterior}/part_{file_number}.txt'
                if os.path.exists(file_path):
                    files_to_merge.append(open(file_path, 'r'))

            output_file_path = os.path.join(caminho_subpasta, f'part_{contadorArquivos}.txt')

            contadorArquivos+=1

            with open(output_file_path, 'w') as output_file:
                merged_lines = []

                # Lê a primeira linha de cada arquivo e armazenar em uma lista
                for file in files_to_merge:
                    line = file.readline()
                    if line:
                        merged_lines.append((line, file))

                while merged_lines:
                    # Encontra a menor linha entre as linhas lidas dos arquivos
                    merged_lines = sorter.quick_sort(merged_lines)
                    smallest_line, smallest_file = merged_lines.pop(0)

                    # Escreve a menor linha no arquivo de saída
                    output_file.write(smallest_line)

                    # Lê a próxima linha do arquivo que teve a menor linha escrita
                    next_line = smallest_file.readline()
                    if next_line:
                        merged_lines.append((next_line, smallest_file))

            for file in files_to_merge:
                file.close()
        
        # Debugging
        print("")
        print(contadorArquivos,"arquivos criados nessa faixa")
        print("Tamanho do minor_files:",AF.contar_arquivos_em_pasta("file_parts/MultiWay/minor_files"))
        print(f"Tamanho do medium_files_{contadorDeIteracoes}:",AF.contar_arquivos_em_pasta(f"file_parts/MultiWay/medium_files_{contadorDeIteracoes}"))

        pasta_anterior = f"medium_files_{contadorDeIteracoes}"
        contadorDeIteracoes+=1

        merge_files(arquivos_por_merge, contadorDeIteracoes, pasta_anterior)
    else:
        os.rename(f"file_parts/MultiWay/{pasta_anterior}/part_0.txt", f"file_parts/MultiWay/{pasta_anterior}/arquivoFinal_ordenado.txt")