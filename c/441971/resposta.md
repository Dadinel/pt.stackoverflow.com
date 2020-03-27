Isso é normal e inclusive esperado.

O prompt fica aberto enquanto seu programa está em execução, ao final ele fecha.


----------


Você pode criar formas dele não fechar de forma imediata, é bem comum utilizar a função `getchar()` como teste, antes do `return` da `main`, assim o programa aguarda a tecla *ENTER* sem pressionada para encerrar:

    #include <stdio.h>
    
    int main(void) {
      printf("Hello world\n");
      getchar();
      return 0;
    }

Com isso, será exibido os dados no prompt, mas a função `getchar` vai *segurar* a execução.

> Veja online: https://repl.it/repls/MedicalCriticalExperiments


----------

Você pode acabar encontrando exemplos que utilizam `system("pause")`, isso também vai segurar a execução do programa, mas só vai funcionar em Windows.
