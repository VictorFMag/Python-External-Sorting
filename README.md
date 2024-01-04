<h1>Sobre o README</h1>
Esse README explicará o funcionamento dos diferentes arquivos e métodos do código.<br>
A ideia é que cada um deles seja abordado de forma isolada e com uma explicação clara e simples sobre as responsabilidades de cada um.<br>
<hr>
<h1>main.py</h1>
O arquivo main.py orquestra a execução dos métodos de ordenação externa, calcula os tempos de execução e realiza uma análise comparativa entre eles, resumindo qual método pode ser mais indicado dependendo das características dos dados e do desempenho encontrado na execução.<br><br>
Além disso, define a instância e a ordem da árvore B necessária para a implementação da parte 3.<br>
<hr>
<h1>auxFunction.py</h1>
Implementa métodos que são utilizados várias vezes ao longo do código, evitando assim a reescrita desnecessária desses trechos de código.
<hr>
<h1>multiWayMerging.py</h1>
Esse arquivo é responsável por dividir um grande arquivo em partes menores de acordo com um número 'linhas_por_arquivo' - definido em main.py -, ordenar essas partes individualmente e, em seguida, mesclar essas partes ordenadas até obter o arquivo final ordenado.
<hr>
<h1>polyphaseMerging.py</h1>
Esse arquivo é responsável por dividir um grande arquivo em um número de 'maxDeArquivos' - definido no main.py - partes menores, ordenar essas partes individualmente e, em seguida, mesclar essas partes ordenadas até obter o arquivo final ordenado.
<hr>
<h1>ordExt_teste.txt</h1>
É o arquivo original e desorganizado a ser ordenado. Contém um número considerável de linhas, cada uma contendo um único número.
