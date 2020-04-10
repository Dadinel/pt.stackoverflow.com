tenho uma string qualquer: 
```
"novamente mais brevemente uma vez claro, claramente demente, igualmente. novamente."
```
executo um regex em js para pegar as palavras terminadas em "mente"
```
var target = $("#content").text();
var exp = /\w+mente/g; // regex ok
var resultado = null;

while (resultado = exp.exec(target)) {
   marcarTexto_adverbio(resultado); // função que coloca uma tag <mark> em volta
};
```
a var 'resultado' passa todos os valores perfeito. Inclusive o "novamente" duplicado no final:

Mas a função que coloca a tag <mark> não coloca no segundo "novamente", ou seja não coloca em palavras repetidas:
```
function marcarTexto_adverbio(target) {
    $("#content").html(function (_, html) {
        return html.replace(target, '<mark>' + target + '</mark>')
    });
}
```
algum erro de lógica na execução dessa função? (já que a array do 'resultados' vai completa, com todas as palavras do regex)
