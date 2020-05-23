O que pode ser feito, é efetuar o `insert` com base em um `select`, para isso, não é necessário nem mesmo criar um `procedure`.


----------

Você criar a estrutura para o `insert`:

    insert into movimentacao_acesso (idm, data, regiao)

Porém não passa o `values` e sim um `select`, onde a ordem dos campos no `select` precisa ser a mesma que você criou para o `insert`, logo ficaria da seguinte forma:

    select id
           , data
           , regiao
        from historico
       where contrato = 142
         and acao = '1';

Juntando tudo, você teria a seguinte instrução SQL:

    insert into movimentacao_acesso (idm, data, regiao)
      select id
           , data
           , regiao
        from historico
       where contrato = 142
         and acao = '1';

> Veja online: http://sqlfiddle.com/#!9/603e706/1
