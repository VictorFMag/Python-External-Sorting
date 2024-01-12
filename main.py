import time
import os

nome_arquivo = 'ordExt_teste.txt'

arquivos_por_merge = 10
lotes = 100

with open(os.path.join(f'analiseComparativa.txt'), 'w') as file: # Limpa o arquivo de análise
    file.truncate(0)
    file.write("Ambos os metodos de ordenacao externa utilizam principalmente o heapsort para ordenar os arquivos em lotes.")

#=================================================================================================
# Parte 1

'''
import multiWayMerging as MWM

inicio = time.time()
MWM.divide_files(nome_arquivo, lotes)
MWM.merge_files(lotes, contadorDeIteracoes=0, pasta_anterior="minor_files")
fim = time.time()
with open(os.path.join(f'analiseComparativa.txt'), 'a') as file:
    file.write(f"\n\nTempo de execucao do MultiWay Merging: {fim-inicio} segundos.\n")
'''
#=================================================================================================
# Parte 2

import polyphaseMerging as PM

inicio = time.time()
PM.divide_files(nome_arquivo, lotes, maxDeArquivos=10)
PM.merge_files(lotes, contadorDeIteracoes=0)
fim = time.time()
with open(os.path.join(f'analiseComparativa.txt'), 'a') as file:
    file.write(f"Tempo de execucao do Polyphase Merging: {fim-inicio} segundos")
    file.write("\n\nO MultiWay Merging executou varias vezes mais lentamente que o Polyphase Merging, alem de consumir muita memoria externa extra no processo.")
    file.write("\nDessa forma, a conclusao e de que o Polyphase Merging e mais indicado na maior parte dos casos testados.")

print("A análise comparativa entre os métodos utilizados pode ser encontrada no arquivo analiseComparativa.txt\n")

#=================================================================================================
# Parte 3

# Implementação da árvore B

from BTrees.Btree import BTree

t = 1000  # Ordem da árvore B (mínimo de chaves por nó - 1)
b_tree = BTree(t)
file_path = './file_parts/Polyphase/arquivoFinal_ordenado.txt'

# Preenchendo a árvore com o arquivo ordenado
try:
    with open(file_path, 'r') as file:
        linha = file.readline()
        while linha:
            value = float(linha.strip())  # Converte para o tipo de dado apropriado
            b_tree.insert(value)
            linha = file.readline()
except FileNotFoundError:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    exit()
except Exception as e:
    print(f"Erro ao processar o arquivo: {e}")
    exit()

# Testando operações na árvore B
search_key = 20
print(f"Buscando por chave {search_key} em Btree: {b_tree.search(search_key)}")

search_key = 0.3206598979232401
print(f"Buscando por chave {search_key} em Btree: {b_tree.search(search_key)}")

remove_key = 0.3206598979232401
print(f"Removendo chave {remove_key} em Btree: {b_tree.remove(remove_key)}")
print(f"Buscando por chave {remove_key} em Btree: {b_tree.search(remove_key)}\n")

# Implementação com árvore B+

from BTrees.BPlusTree import BPlusTree

bplus_tree = BPlusTree(t)
# file_path = './ordExt.txt'
# O arquivo maior demora muito para montar, a ponto do sistema matar o processo antes de finalizar

# Preenchendo a árvore com o arquivo maior
try:
    with open(file_path, 'r') as file:
        linha = file.readline()
        while linha:
            value = float(linha.strip())  # Converte para o tipo de dado apropriado
            bplus_tree.insert(value)
            linha = file.readline()
except FileNotFoundError:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    exit()
except Exception as e:
    print(f"Erro ao processar o arquivo: {e}")
    exit()

# Testando operações na árvore B+
search_key = 20
print(f"Buscando por chave {search_key} em BPlusTree: {bplus_tree.search(search_key)}")

search_key = 0.3206598979232401
print(f"Buscando por chave {search_key} em BPlusTree: {bplus_tree.search(search_key)}")

remove_key = 0.3206598979232401
print(f"Removendo chave {remove_key} em BPlusTree: {bplus_tree.remove(remove_key)}")
print(f"Buscando por chave {remove_key} em BPlusTree: {bplus_tree.search(remove_key)}\n")