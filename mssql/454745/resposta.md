Como você quer trazer os dados da tabela `carteira` mesmo que não existam dados na tabela `ativo`, você deve utilizar o `left join`:



[![A representa a tabela carteira enquanto B representa a tabela ativo][1]][1]

 - **A** = Carteira

 - **B** = Ativo

----------


Logo sua query ficará da seguinte maneira:

    select c.codigo
         , c.nome
         , c.inicio
         , count(a.codigobovespa) as qtde_papeis
      from carteira c left join ativo a
        on c.codigo = a.carteira
     where c.ativa = 'S'
     group by c.codigo, c.nome, c.inicio


> Veja online: http://sqlfiddle.com/#!18/47e794/6


----------

Caso queira compreender melhor sobre join em SQL, recomendo muito a leitura da seguinte pergunta/resposta: https://pt.stackoverflow.com/questions/6441/qual-%c3%a9-a-diferen%c3%a7a-entre-inner-join-e-outer-join

  [1]: https://i.stack.imgur.com/hi7z7.png
