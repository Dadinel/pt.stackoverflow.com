O erro ocorre, pois mesmo o campo `produto_imposto` aceitando nulo, está recebendo um valor, um valor de uma string vazia: `''`.

Para corrigir essa situação, você pode optar por enviar o valor `null` para o campo `produto_imposto`:

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
        null
        );

Ou remover esse campo do insert, já que ele aceita nulo e você não pretende gravar nada:

     INSERT INTO 
        `produtos` 
        ( 
        `produto_cod`, 
        `produto_nome`, 
        `produto_custo`
        ) 
        VALUES 
        ( 
        '03202374756', 
        'Produto teste XYZv2', 
        '100.50'
        );

> Criei um exemplo online: http://sqlfiddle.com/#!9/c0b5c95/1
