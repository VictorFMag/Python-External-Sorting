import multiWayMerging as MWM
import polyphaseMerging as PM

nome_arquivo = 'ordExt_teste.txt'


arquivos_por_merge = 10
lotes = 100

'''
MWM.divide_files(nome_arquivo, lotes)
MWM.merge_files(lotes, contadorDeIteracoes=0, pasta_anterior="minor_files")
'''

maxDeArquivos = 10
PM.divide_files(nome_arquivo, maxDeArquivos, lotes)
PM.merge_files(nome_arquivo, arquivos_por_merge, contadorDeIteracoes=0)
