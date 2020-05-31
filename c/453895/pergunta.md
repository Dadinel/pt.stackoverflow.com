Eu nunca vi esse operador antes, apenas outro parecido `->`, mas não faz sentido no contexto desse código. 

**Código**

    #include <stdio.h>


    int main() {
        int x = 10;
        while (x --> 0) { // x goes to 0
            printf("%d ", x);
        }
    }

**Saída**

    9 8 7 6 5 4 3 2 1 0
