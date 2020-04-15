Para efetuar buscas em um array bidimensional, você também utiliza a função `aScan`, porém como segundo parâmetro você não coloca exatamente o valor que quer encontrar, mas sim um bloco de código contendo um trecho de código advpl contendo o valor que deseja encontrar.


----------


Normalmente você busca colocando como segundo parâmetro o valor que deseja encontrar, certo?
  
    local nPos := aScan( aTest, .F. ) 

Porém como o array é bidimensional, você precisar acessar uma posição específica dele na pesquisa, aí entra o bloco de código:

    local nPos := aScan( aTest, {| aPosArray | aPosArray[3] == .F. } ) 

Como trata-se de um valor booleano, você também pode apenas negar o valor:

    local nPos := aScan( aTest, {| aPosArray | !aPosArray[3] } )


Imagine que esse bloco será executado duas vezes, que é o tamanho do seu array, a variável `aPosArray` vai receber o valor do seu array principal, sendo que na primeira vez ela terá o valor `{ 0, "Teste", .T. }` e na segunda vez o valor `{ 1, "Teste", .F. }`


> *Obs.: É válido ressaltar que advpl os índices começam em 1.*

----------

Seu código completo ficaria mais ou menos da seguinte forma:

    user function pesqArray()
    local aTest as array
    local nPos as numeric

    aTest := { { 0, "Teste", .T. }, { 1, "Teste", .F. } }
    nPos := aScan( aTest, {| aPosArray | !aPosArray[3] } )

    ConOut("O valor foi encontrado na posicao:", nPos)

    return


No exemplo eu também tipei as variáveis, isso ajuda a pegar pequenos erros com base nos warnings que o compilador retorna, já que advpl acaba tendo muito runtime error.

----------

> Documentação:

> https://tdn.totvs.com/display/tec/AScan

> https://tdn.totvs.com/display/tec/Tipagem+de+Dados

> https://tdn.totvs.com/pages/viewpage.action?pageId=6063094
