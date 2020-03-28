Seguindo o seu exemplo, você pode fazer esse filtro no `where`, utilizando um `subselect`:

    select *
      from vendas
     where ven_data <= ( select max(ven_data) from vendas )
       and ven_data >= ( select dateadd(day, -6, max(ven_data)) from vendas );

Utilizei o `max` para obter a ultima venda e novamente o `max` para obter a data de sete dias antes da última venda, com o auxílio da função `dateadd`.


***Obs.:** Coloquei -6 na subtração da data para ficar como seu exemplo, pois dia 10 - 7, seria 3, mas pelo seu exemplo, você quer o dia posterior a esse, isso também pode ser alterado quanto ao `>=` na condição do `where`, mantendo assim 7 na subtração mas a condição fica somente `>`*

----------


> Veja esse exemplo online: http://sqlfiddle.com/#!18/680e7/3


----------


> Documentações: 

> https://docs.microsoft.com/pt-br/sql/t-sql/functions/max-transact-sql?view=sql-server-ver15

> https://docs.microsoft.com/pt-br/sql/t-sql/functions/dateadd-transact-sql?view=sql-server-ver15
