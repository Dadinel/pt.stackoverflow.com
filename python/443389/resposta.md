É bem simples, basta chamar a função `calcular_velocidade` como parâmetro da função `calcular_aceleracao`:

    calcular_aceleracao( calcular_velocidade(20, 2) , 2)

Seu exemplo, ficaria da seguinte forma:

    def calcular_velocidade(distancia, tempo):
      velocidade = distancia / tempo
      return velocidade
    
    def calcular_aceleracao(velocidade, tempo):
      aceleracao = velocidade / tempo
      return aceleracao
    
    aceleracao = calcular_aceleracao(calcular_velocidade(20, 2), 2)
    
    print(aceleracao)

> Veja online: https://repl.it/repls/CompleteGrownDaemons


----------

Também é possível declarar uma variável e assim, armazenar o retorno da função `calcular_velocidade`, utilizando então a variável declarada como argumento para a função `calcular_aceleracao`:

    velocidade = calcular_velocidade(20, 2)
    aceleracao = calcular_aceleracao(velocidade, 2)

Ficando então da seguinte forma:

    def calcular_velocidade(distancia, tempo):
      velocidade = distancia / tempo
      return velocidade
    
    def calcular_aceleracao(velocidade, tempo):
      aceleracao = velocidade / tempo
      return aceleracao
    
    velocidade = calcular_velocidade(20, 2)
    aceleracao = calcular_aceleracao(velocidade, 2)
    
    print(aceleracao)

> Veja online: https://repl.it/repls/CraftyTrustworthyDehardwarization


----------

Perceba que o resultado é exatamente o mesmo, são formas diferentes de trabalhar. Caso você precise utilizar o resultado de `calcular_velocidade` mais de uma vez, declarar a variável pode ser uma opção melhor pare evitar chamadas da mesma função.
