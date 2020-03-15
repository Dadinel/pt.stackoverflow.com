create table produtos (
   id int(11) not null auto_increment
 , produto_cod varchar(15) null
 , produto_nome varchar(80) null
 , produto_custo double(10,2) null
 , produto_imposto double(10,2) null
 , constraint pk_produtos primary key (id) );
 
 
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
