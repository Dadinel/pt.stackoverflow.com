Amigos,

estou tentando fazer um app para controle de investimentos em ações. No DB deste app tenho a tabela carteira e a tabela ativo. Preciso fazer um select que me retorne as carteiras ativas e a quantidade de papeis(ações) que cada carteira tem. Ocorre que a carteira pode estar ativa mas ainda não conter nenhuma ação.

fiz a seguinte consulta:

    select c.codigo, c.nome, c.inicio, COUNT(a.codigobovespa) as qtde_papeis
    from carteira c inner join ativo a
    on c.codigo=a.carteira
    where c.ativa = 'S'
    group by c.codigo, c.nome, c.inicio

Todavia apesar da consulta montar os campos direitinho, ela somente retorna uma carteira, mesmo ativa, se ela contiver um correspondente na tabela ativo. E eu preciso que aparece todas e quantidade zero quando nao houver ativo correspondente na tabela ativo.

Alguem pode me ajudar nessa?!?!
