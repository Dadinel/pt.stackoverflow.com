Na verdade, o que está acontecendo é `x--` maior que `0`, ou seja, o `while` está decrementando `x` enquanto `x` maior que `0`:

    #include <stdio.h>
    
    int main() {
        int x = 10;
    
        while (x-- > 0) { // x goes to 0
            printf("%d ", x);
        }
    
        printf("\nX = %d", x);
    
        return 0;
    }

> Veja online:https://repl.it/@Dadinel/StainedFunnyProcedures#main.c

Perceba que no final do `while`, `x` será `-1`.
