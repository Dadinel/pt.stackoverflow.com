Você não precisa ordenar a lista a cada inserção de dados, pode fazer isso somente no final, pois os métodos `sort` e `reverse` trabalham com todos os dados da lista:

    numeros = []
    
    for i in range(0,3):
        numeros.append(int(input('Digite um numero: : ')))
    
    numeros.sort()
    numeros.reverse()
    
    print('a ordem eh:',numeros)


> Veja online: https://repl.it/repls/DependableDopeyDecompiler

----------

Também é possível fazer a ordenação da lista com apenas uma linha, utilizando o parâmetro `reverse` do método `sort`:

    numeros = []
    
    for i in range(0,3):
        numeros.append(int(input('Digite um numero: : ')))
    
    numeros.sort(reverse=True)
    
    print('a ordem eh:',numeros)

> Veja online: https://repl.it/repls/SwelteringAttractiveAttribute


----------

Se você só precisa exibir a lista ordenada, também seria possível utilizar a função `sorted`, que diferente dos métodos utilizados, recebe uma lista e não altera a mesma, ela retorna uma nova lista ordenada:

    numeros = []
    
    for i in range(0,3):
        numeros.append(int(input('Digite um numero: : ')))
    
    print('a ordem eh:',sorted(numeros, reverse=True))

> Veja online: https://repl.it/repls/VitalFrightenedApplicationsoftware
