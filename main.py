import fileController as FC

nome_arquivo = 'ordExt_teste.txt'
linhas_por_arquivo = 100
arquivos_por_merge = 10
FC.divide_arquivo(nome_arquivo, linhas_por_arquivo)
FC.merge_files(arquivos_por_merge)