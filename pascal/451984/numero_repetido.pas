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
