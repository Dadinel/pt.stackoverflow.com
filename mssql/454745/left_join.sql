select c.codigo
     , c.nome
     , c.inicio
     , count(a.codigobovespa) as qtde_papeis
  from carteira c left join ativo a
    on c.codigo = a.carteira
 where c.ativa = 'S'
 group by c.codigo, c.nome, c.inicio
