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
