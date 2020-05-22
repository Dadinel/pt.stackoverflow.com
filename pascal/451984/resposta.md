Perceba que você pega o número atual digitado:

    valoratual:= numero[i];

E em seu `for` que verifica se o número já existe, você compara com o item que acabou de ser digitado, pois seu `for` varre o array por completo:


    for ii := 1 to 5 do 
    begin
    	if valoratual = numero[ii] then
    	begin;
    		Write('Número já existe, digite outro: ');
    		i:=i-1;
    	end;
    end;


----------

Você pode alterar o seu segundo `for`, para que ele vá de `1` até o `i - 1`, pois seria até a posição anterior a que você está:

    for ii := 1 to ( i - 1 ) do 
    begin
    	if valoratual = numero[ii] then
    	begin;
    		Write('Número já existe, digite outro: ');
    		i := i-1;
    	end;
    end;


----------

Isso corrigirá a questão dos números serem sempre iguais... Mas seu código *não compila no Free Pascal*... pois no seu exemplo, você altera a variável `i` dentro do `for` e isso não é permitido.

Caso você venha a ter esse problema, você pode alterar um pouco mais o código, veja o exemplo:


    program numero_repetido;
    var
        numero: array [1..5] of integer;
        i: integer;
        ii: integer;
        valoratual: integer;
        repetido: boolean;
    begin
        ii := 1;
        i := 1;
        
        for i := 1 to 5 do
        begin
            repetido := true;
        
            while repetido do
            begin
                writeLn('Digite um número inteiro: ');
                read(numero[i]);
                valoratual := numero[i];
                repetido := false;
        
                for ii := 1 to (i - 1) do 
                begin
                    if valoratual = numero[ii] then
                    begin;
                        writeLn('Número já existe, digite outro!');
                        repetido := true;
                    end;
                end;
            end;
        end;
        
        writeLn('Números digitados:');
        
        for i:= 1 to 5 do
        begin
            writeLn(numero[i]);
        end;
    end.

Nesse exemplo eu passei a utilizar o `while` como forma de manter o usuário dentro do loop até que digite um número válido.

> Veja online: http://tpcg.io/1AUKL6zd 
