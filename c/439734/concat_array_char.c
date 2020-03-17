#include <stdio.h>
#include <string.h>

char* concatenar(char frase1[], char frase2[]){
  static char fraseFinal[2000];

  for (int i=0; i < strlen(frase1); i++) {
    if (frase1[i] != '\n')
      fraseFinal[i] = frase1[i];
  }

  int size = strlen(fraseFinal);

  for (int i=0; i < strlen(frase2); i++) {
    if (frase2[i] != '\n')
      fraseFinal[size + i ] = frase2[i];
  }

  return fraseFinal;  
}

int main(){
  char frase1[100];  
  printf("Escreva a 1ª frase: ");  
  fgets(frase1,100,stdin);

  char frase2[100];  
  printf("Escreva a 2ª frase: ");  
  fgets(frase2,100,stdin);  

  printf("Concatenação: %s\n", concatenar(frase1,frase2));
  return 0;
}
