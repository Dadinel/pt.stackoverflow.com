Gostaria de saber porque o meu código esta retornando o valor errado da variável menor : 

	int i, numero[10], menor;

	menor = numero[0];
	
	for (i = 1; i <= 5; i++){
		printf("Entre com o %d numero : \n",i);
		scanf("%d",&numero[i]);
	}
	
	for (i = 1; i<=5; i++){
		if (numero[i] < menor)
			menor = numero[i];
	}

	
	printf("Menor : %d \n",menor);
