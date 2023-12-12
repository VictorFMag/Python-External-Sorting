import auxFunctions as AF
import internalSortingMethods as sorter
import random
import os

def divide_files(nome_arquivo, lotesDeLeitura, maxDeArquivos): # Divide o arquivo a ser ordenado em partes menores de acordo com a quantidade de linhas por arquivo definida em main.py
    AF.criaPasta("file_parts/Polyphase")
    
    if AF.contar_arquivos_em_pasta("file_parts/Polyphase") == 0:

        # Criar os 10 arquivos
        for i in range(1, maxDeArquivos+1):
            with open(os.path.join(f'file_parts/Polyphase/part_{i}.txt'), 'w') as file:
                if i != maxDeArquivos:  # Deixar o último arquivo vazio
                    file.write('')
        
        with open(nome_arquivo, 'r') as arquivo_origem:
            linha = arquivo_origem.readline()
            
            while linha:
                indiceAleatorio = random.randint(1, maxDeArquivos-1)  # Gerar índices de 1 a 9
                with open(f'file_parts/Polyphase/part_{indiceAleatorio}.txt', 'a') as parte_arquivo:
                    contador_linhas = 0
                    menorArr = []
                    
                    while contador_linhas < lotesDeLeitura and linha:
                        menorArr.append(linha)
                        linha = arquivo_origem.readline()
                        contador_linhas += 1
                    
                    sorter.heap_sort(menorArr)
                    parte_arquivo.write("".join(menorArr))
    
    else:
        AF.limpaPasta('file_parts/Polyphase')
        divide_files(nome_arquivo, maxDeArquivos, lotesDeLeitura)

#=======================================================================================================================

import tempfile
import shutil

def merge_files(lotesDeMerge, contadorDeIteracoes): # Isso tá funcionando, mas demora 1 bilhão de anos
    pasta_polyphase = 'file_parts/Polyphase'
    num_arquivos_pasta = AF.contar_arquivos_em_pasta(pasta_polyphase)

    # Encontra o arquivo vazio
    arquivo_vazio = ""
    for i in range(1, num_arquivos_pasta + 1):
        with open(f"{pasta_polyphase}/part_{i}.txt", 'r') as arquivo:
            if not arquivo.read():
                arquivo_vazio = arquivo.name
                break

    if arquivo_vazio!="":
        # Itera sobre os arquivos ordenados em lotes de 'lotesDeMerge'
        for i in range(num_arquivos_pasta):

            # Lista para armazenar os arquivos a serem mesclados nesta iteração
            files_to_merge = []
            for j in range(lotesDeMerge):
                file_number = i + j
                file_path = f'{pasta_polyphase}/part_{file_number}.txt'
                if os.path.exists(file_path):
                    files_to_merge.append(open(file_path, 'r'))

            with open(f'{arquivo_vazio}', 'w') as output_file:
                merged_lines = []

                # Lê a primeira linha de cada arquivo e armazenar em uma lista
                for file in files_to_merge:
                    print("Arquivo to merge:",file)
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
                    
                    # Nome do arquivo original
                    temp_file = tempfile.NamedTemporaryFile(mode='r+', delete=False)
                    # Abre o arquivo original para leitura
                    with open(smallest_file.name, 'r') as file:
                        next(file)  # Pula a primeira linha
                        shutil.copyfileobj(file, temp_file)  # Copia as linhas restantes para o arquivo temporário
                    temp_file.close()  # Fecha o arquivo temporário
                    # Move o conteúdo do arquivo temporário de volta para o arquivo original
                    shutil.move(temp_file.name, smallest_file.name)

                    if next_line:
                        merged_lines.append((next_line, smallest_file))

            for file in files_to_merge:
                file.close()
            
        contadorDeIteracoes+=1
        merge_files(lotesDeMerge, contadorDeIteracoes)
    else:
        os.rename(f"{pasta_polyphase}/{arquivo_vazio}", f"{pasta_polyphase}/arquivoFinal_ordenado.txt")