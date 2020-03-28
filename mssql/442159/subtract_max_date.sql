select *
  from vendas
 where ven_data <= ( select max(ven_data) from vendas )
   and ven_data >= ( select dateadd(day, -6, max(ven_data)) from vendas );
