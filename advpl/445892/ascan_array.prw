
function u_pesqArray()
local aTest as array
local nPos as numeric

aTest := { { 0, "Teste", .T. }, { 1, "Teste", .F. } }
nPos := aScan( aTest, {| aPosArray | !aPosArray[3] } )

ConOut("O valor foi encontrado na posicao:", nPos)

return
