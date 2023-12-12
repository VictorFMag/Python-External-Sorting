import multiWayMerging as MWM
import polyphaseMerging as PM

nome_arquivo = 'ordExt_teste.txt'

arquivos_por_merge = 10
lotes = 100

'''
MWM.divide_files(nome_arquivo, lotes)
MWM.merge_files(lotes, contadorDeIteracoes=0, pasta_anterior="minor_files")
'''

# Exemplo de uso:
input_folder = 'file_parts/Polyphase'
output_file = 'sorted_output.txt'

PM.divide_files(nome_arquivo, lotes, maxDeArquivos=10)
PM.merge_files(lotes, contadorDeIteracoes=0)