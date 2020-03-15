Para agrupar tudo, você precisa fazer duas coisas nessa query:

Utilizar o `SUM` também no cálculo de `TOTAL_VALOR`:

    SUM( dbo.tb_produto.val_produto * dbo.tb_produto.qtd_produto ) AS TOTAL_VALOR

E deixar no group by, apenas o `dbo.tb_municipio.des_municipio`:

    GROUP  BY dbo.tb_municipio.des_municipio


----------

Sua query então ficaria da seguinte forma:

    SELECT dbo.tb_municipio.des_municipio , 
           Sum(dbo.tb_produto.qtd_produto) AS TOTAL_SOMA ,
           Sum( dbo.tb_produto.val_produto * dbo.tb_produto.qtd_produto ) AS TOTAL_VALOR 
     FROM  dbo.tb_municipio 
           INNER JOIN dbo.tb_unidade 
                   ON dbo.tb_municipio.cod_municipio = dbo.tb_unidade.cod_municipio 
           INNER JOIN dbo.tb_produto 
                   ON dbo.tb_unidade.cod_unidade = dbo.tb_produto.cod_unidade 
     WHERE des_produto = 'Omeprazol 10mg' 
     GROUP BY dbo.tb_municipio.des_municipio
