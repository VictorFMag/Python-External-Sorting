import multiWayMerging as MWM
import polyphaseMerging as PM
import time
import os

nome_arquivo = 'ordExt_teste.txt'

arquivos_por_merge = 10
lotes = 100

with open(os.path.join(f'analiseComparativa.txt'), 'w') as file: # Limpa o arquivo de análise
    file.truncate(0)
    file.write("Ambos os metodos de ordenacao externa utilizam principalmente o heapsort para ordenar os arquivos em lotes.")

inicio = time.time()
MWM.divide_files(nome_arquivo, lotes)
MWM.merge_files(lotes, contadorDeIteracoes=0, pasta_anterior="minor_files")
fim = time.time()
with open(os.path.join(f'analiseComparativa.txt'), 'a') as file:
    file.write(f"\n\nTempo de execucao do MultiWay Merging: {fim-inicio} segundos.\n")


inicio = time.time()
PM.divide_files(nome_arquivo, lotes, maxDeArquivos=10)
PM.merge_files(lotes, contadorDeIteracoes=0)
fim = time.time()
with open(os.path.join(f'analiseComparativa.txt'), 'a') as file:
    file.write(f"Tempo de execucao do Polyphase Merging: {fim-inicio} segundos")
    file.write("\n\nO MultiWay Merging executou varias vezes mais lentamente que o Polyphase Merging, alem de consumir muita memoria externa extra no processo.")
    file.write("\nDessa forma, a conclusao e de que o Polyphase Merging e mais indicado na maior parte dos casos testados.")

print("A análise comparativa entre os métodos utilizados pode ser encontrada no arquivo analiseComparativa.txt\n")