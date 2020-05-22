Você precisa converter os números para `double` antes da divisão, em seu exemplo você divide os inteiros e somente depois faz a conversão:

    resultado = (double)(a / b);

Para corrigir e ter um número com decimais, basta converter um dos números antes da divisão, exemplo:

    resultado = (double)a / b;

Com isso sua divisão já terá um resultado `double`, contendo decimais.


----------

Um ponto do seu código que pode ser melhorado é a verificação da operação, caso ela seja diferente de `1`, você faz outros três `ifs`.

Aqui podemos utilizar o `else if`:

    if(operacao == 1){
        resultado = a + b;
        printf("\n%d + %d = %.2f\n", a, b, resultado);
    }
    else if(operacao == 2){
        resultado = a - b;
        printf("\n%d - %d = %.2f\n", a, b, resultado);
    }
    else if(operacao == 3){
        resultado = a * b;
        printf("\n%d X %d = %.2f\n", a, b, resultado);
    }
    else if(operacao == 4){
        resultado = (double)a / b;
        printf("\n%d / %d = %.2f\n", a, b, resultado);
    }

Ou um `switch`:

    switch(operacao) {
      case 1: {
          resultado = a + b;
          printf("\n%d + %d = %.2f\n", a, b, resultado);
          break;
      }
      case 2: {
          resultado = a - b;
          printf("\n%d - %d = %.2f\n", a, b, resultado);
          break;
      }
      case 3: {
          resultado = a * b;
          printf("\n%d X %d = %.2f\n", a, b, resultado);
          break;
      }
      case 4: {
          resultado = (double)a / b;
          printf("\n%d / %d = %.2f\n", a, b, resultado);
          break;
      }
    }


----------

Seu código completo ficará mais ou menos da seguinte forma:

    #include <stdio.h>
    #include <stdlib.h>
    
    int main(){
        int a;
        int b;
        int operacao;
        double resultado;
      
        printf("ESCOLHA DOIS NUMEROS E A OPERACAO QUE SERA FEITA ENTRE ELES\n");
        printf("ESCOLHA O NUMERO A\n");
        scanf("%d", &a);
        printf("ESCOLHA O NUMERO B\n");
        scanf("%d", &b);
        printf("ESCOLHA A OPERACAO\n");
        printf(" 1 = SOMA\n 2 = SUBTRACAO\n 3 = MULTIPLICACAO\n 4 = DIVISAO\n");
        scanf("%d", &operacao);
    
        if(operacao == 1){
            resultado = a + b;
            printf("\n%d + %d = %.2f\n", a, b, resultado);
        }
        else if(operacao == 2){
            resultado = a - b;
            printf("\n%d - %d = %.2f\n", a, b, resultado);
        }
        else if(operacao == 3){
            resultado = a * b;
            printf("\n%d X %d = %.2f\n", a, b, resultado);
        }
        else if(operacao == 4){
            resultado = (double)a / b;
            printf("\n%d / %d = %.2f\n", a, b, resultado);
        }
    
        return 0;
    }

> Veja online: https://repl.it/@Dadinel/ConsciousHospitableBooleanvalue
