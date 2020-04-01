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
