insert into movimentacao_acesso (idm, data, regiao)
  select id
       , data
       , regiao
    from historico
   where contrato = 142
     and acao = '1';
