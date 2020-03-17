#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
	FILE *arq;
	char str[24];
	int count = 0;
	int teste = 0;

	arq = fopen("texto.txt","r+");

	//Variável que armazena a leitura dos IF conforme o arquivo é lido
	char ifs[3] = "  \0"; //Ultima posição é o final da string

	while(fgets(str,sizeof(str),arq) != NULL){
		//Verifico toda a cadeira de caracteres lida do arquivo
		for (int i = 0; i < strlen(str); i++) {
			ifs[0] = ifs[1];
			ifs[1] = str[i];

			//Compara o valor if com o presente na variável ifs
			if (strcmp(ifs, "if") == 0) {
				count++;
			}
		}
	}

	fclose(arq);  
	printf("Qt : %i",count);

	return 0;
}
