<?php
$conn = mysqli_connect("localhost", "root", "root", "CODINGGROUND");

if ($conn) {
    mysqli_query($conn,"drop table if exists produtos_pedido");
    mysqli_query($conn,"create table produtos_pedido (cod int, produto_cod int, quantidade int, pedido_cod int)");
    mysqli_query($conn,"insert into produtos_pedido values (36,70,3,30)");
    mysqli_query($conn,"insert into produtos_pedido values (37,51,1,31)");
    mysqli_query($conn,"insert into produtos_pedido values (38,70,3,31)");
    mysqli_query($conn,"insert into produtos_pedido values (39,51,1,32)");
    mysqli_query($conn,"insert into produtos_pedido values (40,70,1,32)");

    $codPedido = 31;
    $prod = "SELECT * FROM produtos_pedido WHERE pedido_cod = $codPedido";
    $query = mysqli_query($conn,$prod);
    $produtos_pedido = [];

    if ($query) {
        while ($produtos = mysqli_fetch_assoc($query)) {
            array_push($produtos_pedido, $produtos);
            echo "Código = " . $produtos["cod"];
            echo " Produto = " . $produtos["produto_cod"];
            echo " Quantidade = " . $produtos["quantidade"];
            echo " Pedido = " . $produtos["pedido_cod"];
            echo "\n";
        }

        mysqli_free_result($query);
    }

    var_dump($produtos_pedido);
    mysqli_close($conn);
}

?>
