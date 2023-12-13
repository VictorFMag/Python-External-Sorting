<h1>Sobre o README</h1>
Esse README explicará o funcionamento dos diferentes arquivos e métodos do código.<br>
A ideia é que cada um deles seja abordado de forma isolada e com uma explicação clara e simples sobre as responsabilidades de cada um.<br>
<hr>
<h1>main.py</h1>
O arquivo main.py orquestra a execução dos métodos de ordenação externa, calcula os tempos de execução e realiza uma análise comparativa entre eles, resumindo qual método pode ser mais indicado dependendo das características dos dados e do desempenho encontrado na execução.<br>
<hr>
<h1>auxFunction.py</h1>
Implementa métodos que são utilizados várias vezes ao longo do código, evitando assim a reescrita desnecessária de trechos desses código.
<h2>contar_arquivos_em_pasta(caminho_pasta):</h2>
Como o nome diz, conta e retorna a quantidade de arquivos contidos em uma pasta.
<h2>limpaPasta(caminho_pasta):</h2>
Apaga todos os arquivos e subpastas contidos em uma pasta.
<h2>criaPasta(caminho_pasta):</h2>
Verifica se a pasta já existe e caso já exista, apaga o que tiver nela. Se não existir, a cria no caminho especificado.
<h2>encontrar_arquivo_vazio(pasta, num_arquivos):</h2>
Encontra e retorna um arquivo que estiver vazio em um determinado caminho de pasta.<br>
<hr>
<h1>multiWayMerging.py</h1>
Esse arquivo é responsável por dividir um grande arquivo em partes menores de acordo com um número 'linhas_por_arquivo' - definido em main.py -, ordenar essas partes individualmente e, em seguida, mesclar essas partes ordenadas até obter o arquivo final ordenado.
<h2>divide_files(nome_arquivo, linhas_por_arquivo):</h2>
Essa função lida com a divisão de um grande arquivo em partes menores para facilitar a ordenação, através do seguinte passo a passo:<br><br>
1) Verifica se já existem arquivos na pasta onde serão armazenadas as partes menores do arquivo a ser ordenado.<br>
2) Abre o arquivo original e lê linha por linha.<br>
3) Enquanto houver linhas no arquivo original, ele as agrupa em partes menores de acordo com o número de linhas por arquivo definido.<br>
4) Cada parte menor é ordenada usando um algoritmo de ordenação chamado Heap Sort.<br>
5) As partes ordenadas são escritas em arquivos individuais na pasta de partes menores.
<h2>merge_files(arquivos_por_merge, contadorDeIteracoes, pasta_anterior):</h2>
Essa função lida com a fusão (merge) das partes menores ordenadas até formar o arquivo final ordenado, de acordo com o seguinte passo a passo:.<br><br>
1) Verifica quantos arquivos existem na pasta de partes menores ordenadas.<br>
2) Cria uma nova pasta para os arquivos resultantes da mesclagem.<br>
3) Lê os arquivos em lotes, conforme a quantidade definida (arquivos_por_merge).<br>
4) Mescla os arquivos lidos em lotes, ordenando-os e escrevendo o resultado na nova pasta criada.<br>
5) Atualiza as variáveis de controle para a próxima iteração da mesclagem, verificando se ainda é necessário mesclar mais arquivos.<br>
<hr>
<h1>polyphaseMerging.py</h1>
Esse arquivo é responsável por dividir um grande arquivo em um número de 'maxDeArquivos' - definido no main.py - partes menores, ordenar essas partes individualmente e, em seguida, mesclar essas partes ordenadas até obter o arquivo final ordenado.
<h2>divide_files(nome_arquivo, lotesDeLeitura, maxDeArquivos):</h2>
Essa função é responsável por dividir um arquivo grande em partes menores, de acordo com o seguinte passo a passo:<br><br>
1) Verifica se a pasta para armazenar as partes menores existe. Se não, a função cria essa pasta.<br>
2) Cria um número fixo de arquivos vazios na pasta file_parts/Polyphase, exceto o último arquivo, que permanece vazio.<br>
3) Abre o arquivo original e lê linha por linha.<br>
4) Enquanto houver linhas no arquivo original, a função escolhe aleatoriamente um dos arquivos menores e escreve um lote de linhas nesse arquivo escolhido.<br>
5) Cada parte menor é ordenada usando o algoritmo de ordenação Heap Sort.
<h2>merge_files(lotesDeMerge, contadorDeIteracoes):</h2>
Essa função trata da fusão (merge) das partes menores ordenadas até formar o arquivo final ordenado, de acordo com o seguinte passo a passo:<br><br>
1) Verifica se existe algum arquivo vazio na pasta file_parts/Polyphase.<br>
2) Itera sobre os arquivos existentes em lotes definidos por lotesDeMerge e mescla esses arquivos, lendo todas as linhas e ordenando-as.<br>
3) As linhas mescladas e ordenadas são escritas em um arquivo vazio.<br>
4) Após mesclar os arquivos, a função verifica se ainda há algum arquivo vazio. Se sim, continua o processo de mesclagem até que não existam mais arquivos vazios, resultando no arquivo final ordenado.<br>
<hr>
<h1>ordExt_teste.txt</h1>
É o arquivo original e desorganizado a ser ordenado. Contém um número considerável de linhas, cada uma contendo um único número.
