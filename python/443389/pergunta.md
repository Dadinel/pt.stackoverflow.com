Sou novo em Python e não estou conseguindo utilizar um retorno de uma função em outra função na sequência:

Estou colocando um exemplo fictício apenas para descrever minha dúvida:

    def calcular_velocidade(distancia, tempo):
        velocidade = distancia / tempo
        return velocidade

    def calcular_aceleracao(velocidade, tempo):
        aceleracao = velocidade / tempo
        return aceleracao

    calcular_velocidade(20, 2)
    calcular_aceleracao(velocidade, 2)

Como faço para utilizar o valor da variável `velocidade` da função `calcular_velocidade` no lugar do parâmetro `velocidade` da função `calcular_aceleracao` ?
