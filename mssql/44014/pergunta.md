Sou iniciante em linguagem SQL e gostaria de uma ajuda para executar uma query.

Preciso de uma nova coluna com os dados: codigo+tamanho+cor (fiz o concatenar e deu certo)

o problema que não consigo resolver é que a cor precisa ter 3 caracteres, porem tem cores que tem um caracter no id e cores que tem 2 caracteres.

preciso que quando tiver 1 caracter no codigo seja adicionado mais 2 zeros.

e quando tiver 2 caracteres no código seja adicionado mais 1 zero.

Exemplo:

**cod.	cod_novo**
    
- 1		001
- 2		002
- 3		003
- 99		099
    

Query:


    	SELECT
    		"Estoque_Atual"."Ordem_Prod_Serv",
    		"Estoque_Atual"."Ordem_Tamanho",
    		"Estoque_Atual"."Ordem_Cor",
    		"Prod_Serv"."Codigo",
    		"Prod_Serv"."Nome",
    		"Cores"."Nome" AS "nome_cor",
    		"Tamanhos"."Nome" AS "tamanho",
    		"Tamanhos"."Codigo",
    		"Cores"."Codigo",
    		"Estoque_Atual"."Qtde_Estoque_Atual",
    		CONCAT ( "prod_serv"."codigo", "tamanhos"."codigo", '0', "Cores"."codigo"  ) AS GRADE 
    	FROM
    		"Estoque_Atual"
    		INNER JOIN "Prod_Serv" ON "Prod_Serv"."Ordem" = "Estoque_Atual"."Ordem_Prod_Serv"
    		LEFT OUTER JOIN "Tamanhos" ON "Tamanhos"."Ordem" = "Estoque_Atual"."Ordem_Tamanho"
    		LEFT OUTER JOIN "Cores" ON "Cores"."Ordem" = "Estoque_Atual"."Ordem_Cor" 
    	WHERE
    		"Prod_Serv"."Codigo" = '1009'
    		AND "Estoque_atual"."Qtde_Estoque_Atual" > 0
    	GROUP BY
    		"Estoque_Atual"."Ordem",
    		"Estoque_Atual"."Ordem_Prod_Serv",
    		"Estoque_Atual"."Ordem_Tamanho",
    		"Estoque_Atual"."Ordem_Cor",
    		"Estoque_Atual"."Qtde_Estoque_Atual",
    		"Prod_Serv"."Codigo",
    		"Prod_Serv"."Nome",
    		"Cores"."Nome",
    		"Tamanhos"."Nome",
    		"Tamanhos"."Codigo",
       	       "Cores"."Codigo" 
