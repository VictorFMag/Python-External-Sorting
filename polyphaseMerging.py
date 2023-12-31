import auxFunctions as AF
import internalSortingMethods as sorter
import random
import os

def divide_files(nome_arquivo, lotesDeLeitura, maxDeArquivos): # Divide o arquivo a ser ordenado em um número fixo de partes menores, definido em main.py
    AF.criaPasta("file_parts/Polyphase")
    
    if AF.contar_arquivos_em_pasta("file_parts/Polyphase") == 0:

        # Cria os 10 arquivos
        for i in range(1, maxDeArquivos+1):
            with open(os.path.join(f'file_parts/Polyphase/part_{i}.txt'), 'w') as file:
                if i != maxDeArquivos:  # Deixa o último arquivo vazio
                    file.write('')
        
        with open(nome_arquivo, 'r') as arquivo_origem:
            linha = arquivo_origem.readline()
            
            while linha:
                indiceAleatorio = random.randint(1, maxDeArquivos-1)  # Gera índices aleatórios de 1 a 9
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

def merge_files(lotesDeMerge, contadorDeIteracoes):
    pasta_polyphase = 'file_parts/Polyphase'
    num_arquivos_pasta = AF.contar_arquivos_em_pasta(pasta_polyphase)

    arquivo_vazio = AF.encontrar_arquivo_vazio(pasta_polyphase, num_arquivos_pasta)

    if arquivo_vazio != "":
        for i in range(0, num_arquivos_pasta, lotesDeMerge):
            files_to_merge = []
            for j in range(lotesDeMerge):
                file_number = i + j
                file_path = f'{pasta_polyphase}/part_{file_number}.txt'
                if os.path.exists(file_path):
                    files_to_merge.append(open(file_path, 'r'))

            merged_lines = []
            for file in files_to_merge:
                lines = file.readlines()  # Lê todas as linhas do arquivo
                if lines:
                    merged_lines.extend(lines) # O extend adiciona vários elementos ao final da lista, ao contrário do append que é só 1

            sorter.heap_sort(merged_lines)

            with open(f'{arquivo_vazio}', 'a') as output_file:
                output_file.writelines(merged_lines)  # Escreve todas as linhas ordenadas no arquivo final

        for file in files_to_merge:
            file.close()

        contadorDeIteracoes += 1
        merge_files(lotesDeMerge, contadorDeIteracoes)
    else:
        os.rename(f"{pasta_polyphase}/part_{num_arquivos_pasta}.txt", f"{pasta_polyphase}/arquivoFinal_ordenado.txt")
        print("\nO arquivo ordenado pode ser encontrado em arquivoFinal_ordenado.txt")