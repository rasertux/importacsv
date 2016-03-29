# importacsv
ImportaCSV é um utilitário para importar, remover ou atualizar dados a partir de arquivos
CSV para o banco de dados MySQL ou MariaDB.<br>
<br>
A primeira linha da coluna do arquivo CSV deve possuir os nomes dos campos da tabela.<br>
<br>
A sintaxe do ImportaCSV é: python main.py path tabela<br>
Onde path é o caminho para o arquivo<br>
tabela é o nome da tabela no banco de dados.<br>
<br>
Em ambientes UNIX é possivel dar permissão de execução ao main.py com: chmod +x main.py<br>
e executa-lo com: ./main.py path tabela<br>
<br>
Tambêm é possivel usar o pypy3: pypy3 main.py path tabela<br>
