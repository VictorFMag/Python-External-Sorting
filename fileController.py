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

    cont = 0
    for i in range(0, contar_arquivos_em_pasta('file_parts/minor_files')-10, 10):
        print("Faixa analisada:",i,"até",i+9)
        with open(f'file_parts/minor_files/parte_{i}.txt', 'r') as file0:
            with open(f'file_parts/minor_files/parte_{i+1}.txt', 'r') as file1:
                with open(f'file_parts/minor_files/parte_{i+2}.txt', 'r') as file2:
                    with open(f'file_parts/minor_files/parte_{i+3}.txt', 'r') as file3:
                        with open(f'file_parts/minor_files/parte_{i+4}.txt', 'r') as file4:
                            with open(f'file_parts/minor_files/parte_{i+5}.txt', 'r') as file5:
                                with open(f'file_parts/minor_files/parte_{i+6}.txt', 'r') as file6:
                                    with open(f'file_parts/minor_files/parte_{i+7}.txt', 'r') as file7:
                                        with open(f'file_parts/minor_files/parte_{i+8}.txt', 'r') as file8:
                                            with open(f'file_parts/minor_files/parte_{i+9}.txt', 'r') as file9:
                                                linhasCandidatasAMerge = []

                                                linha0 = file0.readline()
                                                linha1 = file1.readline()
                                                linha2 = file2.readline()
                                                linha3 = file3.readline()
                                                linha4 = file4.readline()
                                                linha5 = file5.readline()
                                                linha6 = file6.readline()
                                                linha7 = file7.readline()
                                                linha8 = file8.readline()
                                                linha9 = file9.readline()

                                                cont0, cont1, cont2, cont3, cont4, cont5, cont6, cont7, cont8, cont9 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1

                                                linhasCandidatasAMerge.append(linha0)
                                                linhasCandidatasAMerge.append(linha1)
                                                linhasCandidatasAMerge.append(linha2)
                                                linhasCandidatasAMerge.append(linha3)
                                                linhasCandidatasAMerge.append(linha4)
                                                linhasCandidatasAMerge.append(linha5)
                                                linhasCandidatasAMerge.append(linha6)
                                                linhasCandidatasAMerge.append(linha7)
                                                linhasCandidatasAMerge.append(linha8)
                                                linhasCandidatasAMerge.append(linha9)
                                                #print("Array de linhas:",linhasCandidatasAMerge)

                                                nome_arquivo_medio = os.path.join(caminho_subpasta, f'parte_media_{cont}.txt') # Cria os arquivos dentro da pasta
                                                if nome_arquivo_medio:
                                                    print("arquivo médio criado")
                                                
                                                with open(nome_arquivo_medio, 'w') as arquivo_medio:
                                                    while(linhasCandidatasAMerge):
                                                        menor = min(linhasCandidatasAMerge)
                                                        print("menor: ",menor)
                                                        idxArquivoQueContemOMenorNumero = linhasCandidatasAMerge.index(menor)
                                                        print("indiceDoMenorElemento: ",idxArquivoQueContemOMenorNumero)

                                                        arquivo_medio.write(menor)
                                                        
                                                        match idxArquivoQueContemOMenorNumero:
                                                            case 0:
                                                                aux = menor
                                                                for i in range(cont0):
                                                                    linha0 = file0.readline()
                                                                cont0+=1
                                                                if linha0:
                                                                    linhasCandidatasAMerge[idxArquivoQueContemOMenorNumero] = linha0
                                                                else:
                                                                    linhasCandidatasAMerge.remove(aux)
                                                                print(linhasCandidatasAMerge)
                                                            case 1:
                                                                aux = menor
                                                                for i in range(cont1):
                                                                    linha1 = file1.readline()
                                                                cont1+=1
                                                                if linha1:
                                                                    linhasCandidatasAMerge[idxArquivoQueContemOMenorNumero] = linha1
                                                                else:
                                                                    linhasCandidatasAMerge.remove(aux)
                                                                print(linhasCandidatasAMerge)
                                                            case 2:
                                                                aux = menor
                                                                for i in range(cont2):
                                                                    linha2 = file2.readline()
                                                                cont2+=1
                                                                if linha2:
                                                                    linhasCandidatasAMerge[idxArquivoQueContemOMenorNumero] = linha2
                                                                else:
                                                                    linhasCandidatasAMerge.remove(aux)
                                                                print(linhasCandidatasAMerge)
                                                            case 3:
                                                                aux = menor
                                                                for i in range(cont3):
                                                                    linha3 = file3.readline()
                                                                cont3+=1
                                                                if linha3:
                                                                    linhasCandidatasAMerge[idxArquivoQueContemOMenorNumero] = linha3
                                                                else:
                                                                    linhasCandidatasAMerge.remove(aux)
                                                                print(linhasCandidatasAMerge)
                                                            case 4:
                                                                aux = menor
                                                                for i in range(cont4):
                                                                    linha4 = file4.readline()
                                                                cont4+=1
                                                                if linha4:
                                                                    linhasCandidatasAMerge[idxArquivoQueContemOMenorNumero] = linha4
                                                                else:
                                                                    linhasCandidatasAMerge.remove(aux)
                                                                print(linhasCandidatasAMerge)
                                                            case 5:
                                                                aux = menor
                                                                for i in range(cont5):
                                                                    linha5 = file5.readline()
                                                                cont5+=1
                                                                if linha5:
                                                                    linhasCandidatasAMerge[idxArquivoQueContemOMenorNumero] = linha5
                                                                else:
                                                                    linhasCandidatasAMerge.remove(aux)
                                                                print(linhasCandidatasAMerge)
                                                            case 6:
                                                                aux = menor
                                                                for i in range(cont6):
                                                                    linha6 = file6.readline()
                                                                cont6+=1
                                                                if linha6:
                                                                    linhasCandidatasAMerge[idxArquivoQueContemOMenorNumero] = linha6
                                                                else:
                                                                    linhasCandidatasAMerge.remove(aux)
                                                                print(linhasCandidatasAMerge)
                                                            case 7:
                                                                aux = menor
                                                                for i in range(cont7):
                                                                    linha7 = file7.readline()
                                                                cont7+=1
                                                                if linha7:
                                                                    linhasCandidatasAMerge[idxArquivoQueContemOMenorNumero] = linha7
                                                                else:
                                                                    linhasCandidatasAMerge.remove(aux)
                                                                print(linhasCandidatasAMerge)
                                                            case 8:
                                                                aux = menor
                                                                for i in range(cont8):
                                                                    linha8 = file8.readline()
                                                                cont8+=1
                                                                if linha8:
                                                                    linhasCandidatasAMerge[idxArquivoQueContemOMenorNumero] = linha8
                                                                else:
                                                                    linhasCandidatasAMerge.remove(aux)
                                                                print(linhasCandidatasAMerge)
                                                            case 9:
                                                                aux = menor
                                                                for i in range(cont9):
                                                                    linha9 = file9.readline()
                                                                cont9+=1
                                                                if linha9:
                                                                    linhasCandidatasAMerge[idxArquivoQueContemOMenorNumero] = linha9
                                                                else:
                                                                    linhasCandidatasAMerge.remove(aux)
                                                                print(linhasCandidatasAMerge)
                                                            case _:
                                                                "Erro: linha não existe!"
                                                cont+=1
        print("===========================================================================================================================")