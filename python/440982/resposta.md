Existe alguns problemas, como o seu `range` que está aumentando (dobrando) a quantidade de termos:

    range(n+n)

Para pegar os valores, basta acessar a variável do loop, você já faz isso, mas apenas imprime o conteúdo dela:

    print(i)


----------


Para somar os termos, você vai precisar de uma outra variável, vamos criar ela com o valor de zero e chamar ela de soma, pra ficar bem evidente seu intuito:

    soma = 0

No `for`, vamos utilizar ele de 1 até o termo:

    for i in range(1, n+1):

Agora dentro do `for`, vamos somar o valor na variável `soma` sempre que o mesmo for ímpar;

    if i%2>0:
      soma += i

E por fim, apenas imprimimos o valor da variável `soma`:

    print(soma)


----------

Juntando tudo, o código ficará da seguinte forma:

    n = int(input("Digite o número de termos:"))
    soma = 0
    
    for i in range(1, n+1):
      if i%2 > 0:
        soma += i
    
    print(soma)


----------

> Veja online: https://repl.it/repls/RashFortunateLevels
