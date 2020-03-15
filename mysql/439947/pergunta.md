Uma tabela do banco de dados tem 5 colunas.

1ª id autoincremento [INT[11] NOT NULL]
2ª código do produto [varchar(15) NULL]
3ª nome do produto [varchar[80] NULL]
4ª custo do produto [double[10,2] NULL]
5ª imposto do produto [double[10,2] NULL]

[![Estrutura da tabela][1]][1]

[![Índices][2]][2]

Executando o SQL abaixo:

    INSERT INTO 
        `produtos` 
        ( 
        `produto_cod`, 
        `produto_nome`, 
        `produto_custo`, 
        `produto_imposto` 
        ) 
        VALUES 
        ( 
        '03202374756', 
        'Produto teste XYZv2', 
        '100.50', 
        '' 
        );

O campo "imposto do produto" não é obrigatório, e pode-se passar o valor em branco, mas o SQL retorna um erro mesmo o campo sendo um valor `NULL`.

> Data truncated for column 'prod_imposto_ipi'.


  [1]: https://i.stack.imgur.com/tLmIK.png
  [2]: https://i.stack.imgur.com/9BQLu.png
