import auxFunctions as AF
import internalSortingMethods as sorter
import random
import os

def divide_files(nome_arquivo, maxDeArquivos, lotesDeLeitura): # Divide o arquivo a ser ordenado em partes menores de acordo com a quantidade de linhas por arquivo definida em main.py
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

def merge_files(nome_arquivo, lotesDeMerge, contadorDeIteracoes):
    num_arquivos_pasta = AF.contar_arquivos_em_pasta(f'file_parts/Polyphase')
    
    arquivoVazio = ""
    for i in range(1, AF.contar_arquivos_em_pasta("file_parts/Polyphase")+1, 1):
        with open(f"file_parts/Polyphase/part_{i}.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
            if len(linhas)==0:
                arquivoVazio = arquivo.name
                print(arquivoVazio)

    # Itera sobre os arquivos ordenados em lotes de 'lotes'
    for i in range(0, num_arquivos_pasta, lotesDeMerge):

        # Lista para armazenar os arquivos a serem mesclados nesta iteração
        file_list = os.listdir("file_parts/Polyphase")
        files_to_merge = []
        for file in file_list:
            files_to_merge.append(open(f'file_parts/Polyphase/{file}', 'r'))

        with open(arquivoVazio, 'w') as output_file:
            merged_lines = []

            # Lê a primeira linha de cada arquivo e armazenar em uma lista
            for file in files_to_merge:
                for j in range(lotesDeMerge):
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
        
    contadorDeIteracoes+=1

    # Tá dando errado aqui
    with open(arquivoVazio, 'r'):
        with open(nome_arquivo, 'r'):
            numLinhasArquivoVazio = arquivoVazio.readlines()
            numLinhasArquivoOriginal = nome_arquivo.readlines()
    
    if len(numLinhasArquivoOriginal) != len(numLinhasArquivoVazio):
        merge_files(nome_arquivo, lotesDeMerge, contadorDeIteracoes)
