O código está certo, acontece que se sua query retorna mais de uma linha, você precisa chamar a função `mysqli_fetch_assoc` dentro de um laço, para pegar assim todas as linhas retornadas:

    while ($produtos=mysqli_fetch_assoc($query)) {
      //Código
    }


----------

Para colocar os resultados em um array, você pode optar por algo assim:

    $produtos_pedido = [];
    
    while ($produtos = mysqli_fetch_assoc($query)) {
      array_push($produtos_pedido, $produtos);
    }

Sendo `$produtos_pedido` o array que vai conter todos os registros que a query retornou (linhas e colunas)


----------

Se você pretende utilizar os dados durante o loop, no exemplo apenas exibir os valores:

    while ($produtos = mysqli_fetch_assoc($query)) {
    	echo "Código = " . $produtos["cod"];
    	echo " Produto = " . $produtos["produto_cod"];
    	echo " Quantidade = " . $produtos["quantidade"];
    	echo " Pedido = " . $produtos["pedido_cod"];
    	echo "\n";
    }


----------

> Veja um exemplo online:  http://tpcg.io/mTWZdhYB 

> Documentação: https://www.php.net/manual/pt_BR/mysqli-result.fetch-assoc.php
