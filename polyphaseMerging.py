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

def merge_files(nome_arquivo, lotesDeMerge, contadorDeIteracoes): # Isso tá funcionando, mas não da forma que eu queria
    pasta_polyphase = 'file_parts/Polyphase'
    num_arquivos_pasta = AF.contar_arquivos_em_pasta(pasta_polyphase)

    # Encontra o arquivo vazio
    arquivo_vazio = ""
    for i in range(1, num_arquivos_pasta + 1):
        with open(f"{pasta_polyphase}/part_{i}.txt", 'r') as arquivo:
            if not arquivo.read():
                arquivo_vazio = arquivo.name
                break

    # Itera sobre os lotes de arquivos a serem mesclados
    for i in range(0, num_arquivos_pasta, lotesDeMerge):
        files_to_merge = [
            open(f'{pasta_polyphase}/part_{j}.txt', 'r') for j in range(i + 1, min(i + lotesDeMerge + 1, num_arquivos_pasta + 1))
        ]
        
        with open(arquivo_vazio, 'w') as output_file:
            merged_lines = []
            for file in files_to_merge:
                lines = file.readlines()
                if lines:
                    merged_lines.extend(lines)

            sorter.heap_sort(merged_lines)  # Ordena todas as linhas juntas

            # Escreve as linhas ordenadas no arquivo de saída
            output_file.write("".join(merged_lines))

        for file in files_to_merge:
            file.close()

    # Verifica se a mesclagem foi concluída
    with open(arquivo_vazio, 'r') as arquivo_vazio:
        with open(nome_arquivo, 'r') as arquivo_original:
            num_linhas_arquivo_vazio = arquivo_vazio.readlines()
            num_linhas_arquivo_original = arquivo_original.readlines()

    # Se a mesclagem não estiver completa, chama recursivamente merge_files
    if len(num_linhas_arquivo_original) != len(num_linhas_arquivo_vazio):
        contadorDeIteracoes += 1
        merge_files(nome_arquivo, lotesDeMerge, contadorDeIteracoes)