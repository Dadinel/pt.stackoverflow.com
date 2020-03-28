Galera sou iniciante em SQL e tá complicado de resolver esse problema que surgiu.. Preciso de um select no SQL-Server que retorne: as vendas dos últimos sete dias. 

Por exemplo se o último dia em que houve venda, foi no dia 10/04/2019, então a query deverá mostrar as vendas entre o dia 04/04/2019 e 10/04/2019.

A lógica creio eu que esteja correta, porém não sei os comandos adequados para fazer esse select... Valeu ai quem puder me auxiliar!! :D

```
SELECT * FROM vendas
	where ven_data <= max(ven_data)
	and ven_data >= max(ven_data - 7)
```


