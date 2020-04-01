Existem várias formas de fazer isso.

Você pode criar uma variável que recebe o retorno da função `sorted` e então acessar os índices do array:

    raizes = [10, 5]
    
    raizesParaExibir = sorted(raizes)
    
    print(f"A função tem duas raízes reais, que são: {raizesParaExibir[0]} e {raizesParaExibir[1]}.")

Seguindo a mesma lógica, você pode ordenar a lista `raizes` com o método `sort` e então acessar os índices:

    raizes = [10, 5]

    raizes.sort()
    
    print(f"A função tem duas raízes reais, que são: {raizes[0]} e {raizes[1]}.")

Podemos transformar a lista em uma string e remover os colchetes com o método `strip`:

    raizes = [10, 5]
    
    print(f"A função tem duas raízes reais, que são: {str(sorted(raizes)).strip('[]')}.")

Novamente, seguindo essa lógica, podemos remover os colchetes utilizando o método `replace`:

    raizes = [10, 5]
    
    print(f"A função tem duas raízes reais, que são: {str(sorted(raizes)).replace('[', '').replace(']', '')}.")

Como ultimo exemplo, podemos utilizar o método `join` da string em conjunto com a função `map`:

    raizes = [10, 5]
    
    print(f"A função tem duas raízes reais, que são: {', '.join(map(lambda x: str(x), sorted(raizes)))}.")


----------

> Veja todos esses exemplos online: https://repl.it/repls/SeagreenGiddyBruteforceprogramming
