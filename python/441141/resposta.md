O problema está na forma que você está efetuando a leitura do arquivo csv.


----------


No seguinte trecho:

    csv_data = csv.reader('/Users/eduardoaandrad/Dropbox/Desenv/Script/csv/carga_teste.csv',delimiter=';')

O arquivo informado está sendo interpretado como uma string, literalmente, com isso o seu loop gera uma saída completamente diferente do esperado na instrução SQL.

Veja esse trecho de leitura do CSV isolado:

    import csv
    
    csv_data = csv.reader('carga_teste.csv',delimiter=';')
    
    for row in csv_data:
        print(type(row), row)

Mesmo que o arquivo não exista, o código será executado exibindo o nome do arquivo no console, gerando uma lista para cada letra:

> Veja online o resultado: https://repl.it/repls/WetShyRadius


----------

Para corrigir essa situação, você deve abrir o arquivo com a função `open` e o retorno da função `open` será o parâmetro para o `reader` do `csv`:

    import csv
    
    with open("carga_teste.csv") as csvFile:
      csv_data = csv.reader(csvFile, delimiter=';')
    
      for row in csv_data:
          print(row)

> Veja a diferença online: https://repl.it/repls/DeadInnocentOutlier


Efetuei essas correções no código e os dados foram corretamente inseridos.

----------

> Documentação: https://docs.python.org/3/library/csv.html
