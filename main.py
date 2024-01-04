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

import multiWayMerging as MWM

inicio = time.time()
MWM.divide_files(nome_arquivo, lotes)
MWM.merge_files(lotes, contadorDeIteracoes=0, pasta_anterior="minor_files")
fim = time.time()
with open(os.path.join(f'analiseComparativa.txt'), 'a') as file:
    file.write(f"\n\nTempo de execucao do MultiWay Merging: {fim-inicio} segundos.\n")

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

# Etapas 1 e 2 -> implementação da árvore B + testes

from Parte_3.Btree import BTree

t = 1000  # Ordem da árvore B (mínimo de chaves por nó - 1)
b_tree = BTree(t)
file_path = './file_parts/Polyphase/arquivoFinal_ordenado.txt'  # Substitua pelo caminho correto do seu arquivo
page_size = 4096  # Tamanho da página em bytes

with open(file_path, 'r') as file:
    linha = file.readline()
    while linha:
        value = float(linha.strip())  # Converte para o tipo de dado apropriado
        b_tree.insert(value)
        linha = file.readline()

print(b_tree.search(20)) # Chave não encontrada
print(b_tree.search(0.00010279248861089219)) # Chave encontrada

print()

print(b_tree.remove(0.00010279248861089219)) # Valor removido
print(b_tree.search(0.00010279248861089219)) # Chave não encontrada

# Etapa 3 -> Montagem particionada

