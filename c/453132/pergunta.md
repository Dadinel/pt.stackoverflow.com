eu pesquisei aqui no fórum e vi perguntas similares, mas não consegui resolver o problema.

Exercício: "Implemente uma calculadora. O programa deve pedir 3 números ao usuário: 'a', 'b' e 'operação'. Se 'operação' for igual a 1, você deverá imprimir a soma de 'a + b'. Se ela for 2, a subtração. se for 3, a multiplicação. Se for 4, a divisão."

Eu já declarei 'a', 'b' e 'resultado' todos como double, como float, como int, e nunca da certo.

O código está assim:

    #include <stdio.h>
    #include <stdlib.h>
    int main(){
        int a;
        int b;
        int operacao;
        double resultado;
        printf("ESCOLHA DOIS NUMEROS E A OPERACAO QUE SERA FEITA ENTRE 
                ELES\n");
        printf("ESCOLHA O NUMERO A\n");
        scanf("%d", &a);
        printf("ESCOLHA O NUMERO B\n");
        scanf("%d", &b);
        printf("ESCOLHA A OPERACAO\n");
        printf(" 1 = SOMA\n 2 = SUBTRACAO\n 3 = MULTIPLICACAO\n 4 = 
               DIVISAO\n");
        scanf("%d", &operacao);
        if(operacao == 1){
            resultado = a + b;
            printf("\n%d + %d = %.2f\n", a, b, resultado);
        }else{
            if(operacao == 2){
                resultado = a - b;
                printf("\n%d - %d = %.2f\n", a, b, resultado);
            }
            if(operacao == 3){
                resultado = a * b;
                printf("\n%d X %d = %.2f\n", a, b, resultado);
            }
            if(operacao == 4){
                resultado = (double)(a / b);
                printf("\n%d / %d = %.2f\n", a, b, resultado);
     }  }  }

Nesse formato ele funciona perfeitamente quando o resultado é um número inteiro, mas quando o resultado é decimal só aparecem zeros depois da virgula.

Quando eu declarei as variáveis como double ou float o programa só imprimia zeros...

Desculpa se essa pergunta é muito recorrente, mas eu realmente não consegui, e já olhei todas as respostas que poderiam me ajudar.
