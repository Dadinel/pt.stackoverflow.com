Você tem diversos problemas aqui.

Quando você declara uma variável em C e não atribui um valor, ela pode conter um lixo de memória, ou seja, seu array `numero[10]` pode conter dezenas de valores que você nem faz ideia, leia mais sobre isso aqui:

> https://pt.stackoverflow.com/questions/217530/por-que-geralmente-se-declara-uma-vari%C3%A1vel-com-valor-padr%C3%A3o

Você pode inicializar o seu array na declaração, da seguinte forma:

    int numero[10] = {0,0,0,0,0,0,0,0,0,0};

Com isso, você não terá mais o problema de valores indesejados, mas perceba o seguinte, você tem um array de 10 posições, mas utiliza somente 5... Logo mesmo inicializando o array, caso o usuário não digite nenhuma número negativo, o menor valor sempre será 0, pois existem 5 posições com esse valor no array.

Podemos então, diminuir o array:

    int numero[5] = {0,0,0,0,0};

E também corrigir o `for` para que faça a iteração desde a posição 0 do array, caso não saiba, é uma informação bem importante, array em C começa em 0, logo um array de 5 posições, começa em 0 e acaba em 4:

    for (i = 0; i < 5; i++){
        printf("Entre com o %d numero : \n",i+1);
        scanf("%d",&numero[i]);
    }


Perceba que começo em 0, para exibir o número correto ao usuário, somo 1 no índice do array no `printf`.

Também iniciamos a variável `menor` após o `for`, para que ela já tenha um valor presente no array:

    menor = numero[0];

E por fim, corrigimos o for que busca o menor valor no array, como já temos o valor da primeira posição do array, podemos começar esse for em 1:

    for (i = 1; i < 5; i++){
        if (numero[i] < menor)
            menor = numero[i];
    }

***Obs.:** Como agora trabalhamos com todas as posições do array e inicializamos a variável `menor` após o for, os valores de inicialização do array `numero` podem ser removidos e você terá o mesmo resultado, pois não utilizou o array antes de sobrescrever todos os seus valores, mas achei válido citar, veja esse exemplo online para ver e compreender melhor os valores que citei: https://repl.it/repls/FineOffshoreDatabases*


----------

Seu código final, vai ficar mais ou menos da seguinte forma:

    #include <stdio.h>
    
    int main(void) {
        int i, menor;
        int numero[5] = {0,0,0,0,0};
    
        for (i = 0; i < 5; i++){
            printf("Entre com o %d numero : \n",i+1);
            scanf("%d",&numero[i]);
        }
    
        menor = numero[0];
    
        for (i = 1; i < 5; i++){
            if (numero[i] < menor)
                menor = numero[i];
        }
    
        printf("Menor : %d \n",menor);
    
        return 0;
    }

> Veja online: https://repl.it/repls/OblongAnguishedMicrokernel


----------

Se quiser saber mais sobre o porque do array começar em 0, leia aqui:

> https://pt.stackoverflow.com/questions/183798/por-que-o-%c3%adndice-de-arrays-e-outras-sequ%c3%aancias-come%c3%a7am-pelo-zero
