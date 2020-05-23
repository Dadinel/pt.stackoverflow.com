Eu tenho uma aplicação que desenvolvi a alguns anos atrás na pressa, e só depois comecei a trabalhar para melhorar o desempenho dele.
Neste app, tem uma parte do processo que eu executo várias ações seguidas no banco, inicialmente meu plano era colocar numa procedure mas eu tive um problema, que era não conseguir tratar linha por linha de um select no MySQL (para exibição de relatório), e devido a falta de tempo pra estudar o resolvi tratando no backend diretamente com python. 

Hoje tenho o mesmo cenário, preciso gerar um relatório a partir de dados de outra tabela mas preciso ler linha por linha e não queria fazer isso com python, porque aumentaria processos tem alguma forma de fazer isso numa procedure?

Eu poderia fazer um loop definindo o `limit` a cada volta para tratar as linhas, mas queria saber se é possível fazer com menos código, dentro de uma procedure, tipo:

```MySQL
while (select `acao`,`regiao`,`id`,`data` into @acao, @regiao, @id, @data 
       from `historico` where `contrato` = '142';) Do

       if (@acao == '1') then 
           insert into movimentacao_acesso (`idm`, `data`, `regiao`) values (@id, @data, @regiao); 
       end if;

end while;

select * from movimentacao_acesso;
```

Desde já agradeço. Só preciso rodar esse loop na procedure
