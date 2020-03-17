Quero exibir os produtos que tenham o mesmo código de pedido, porém quando faço o select ele exibe apenas o primeiro produto que encontra com aquele código.

    $prod = "SELECT * FROM produtos_pedido WHERE pedido_cod = $codPedido";
    $query = mysqli_query($conn,$prod);
    $produtos=mysqli_fetch_assoc($query);

[![Banco de dados tabela produtos_pedido][1]][1]


  [1]: https://i.stack.imgur.com/XO3Da.png
