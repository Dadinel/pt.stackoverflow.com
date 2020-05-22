Olá, preciso fazer um programa que o usuário digite 5 números e caso um desses números seja repetido, peça para que o usuário digite novamente outro número, porém qualquer número que eu digito aparece que é repetido. Meu código:
 

       program numero_repetido;
        var
           numero: array [1..5] of integer;
           i: integer;
        	 ii: integer;
           valoratual:integer;
        begin
        ii:= 1;
        i:=1;
        for i:= 1 to 5 do
        	begin
        		if i > 0 then
        		begin
        		 Write('Digite um número inteiro: ');
        		 read(numero[i]);
        		 
        		 valoratual:= numero[i];
        		 
        			for ii:=1 to 5 do 
        				begin
        					if valoratual = numero[ii] then
        						begin;
        							Write('Número já existe, digite outro: ');
        							i:=i-1;
        													
        						end;
        				end;
        		end
        		else
        		begin
        			Write('Digite um número inteirooo: ');
        			read(numero[i]);
        		end;			
        	end;
         
        for i:= 1 to 5 do
        	begin
        		writeLN(numero[i]);
        	end;
     
       END.
