Para não permitir valores nulos, na criação do campo, basta informar `not null`, exemplo:

    CREATE TABLE fornecedor (
      cd_fornecedor SERIAL PRIMARY KEY,
      cd_endereco_fornecedor INT not null,
      cd_telefone_fornecedor INT not null,
      cnpj_fornecedor VARCHAR(18),
      nome_fornecedor VARCHAR(30),
      email_fornecedor VARCHAR(50),
      foreign key (cd_endereco_fornecedor) references endereco_fornecedor (cd_endereco_fornecedor),
      foreign key (cd_telefone_fornecedor) references telefone_fornecedor (cd_telefone_fornecedor)  
    );

> Veja online: http://sqlfiddle.com/#!17/4b6e9


----------

Caso deseje outros campos com tal condição, basta seguir a sintaxe:

    nome_do_campo tipo_do_campo not null


----------

> Documentação: https://www.postgresql.org/docs/9.4/ddl-constraints.html
