É possível fazer um `replicate` de `'0'` conforme o tamanho (`len`) do valor presente no campo:

    concat(replicate('0', 3 - len(campo)),campo) as meu_novo_campo


----------

Com o seu campo, ficaria da seguinte forma:

    concat(replicate('0', 3 - len("Cores"."codigo")),"Cores"."codigo")
Juntando com os demais campos:

    CONCAT ( "prod_serv"."codigo", "tamanhos"."codigo", concat(replicate('0', 3 - len("Cores"."codigo")),"Cores"."codigo") ) AS GRADE


----------


> Veja um exemplo online: http://sqlfiddle.com/#!18/ffa2f/7
