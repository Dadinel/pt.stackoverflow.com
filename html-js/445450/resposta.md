Existe um problema, o `replace` está efetuando apenas uma substituição da maneira que está sendo utilizado, ao encontrar a primeira ocorrência ele substitui e acabou... Como você tem duas palavras iguais, ele substitui exatamente a mesma palavra duas vezes.

Se você inspecionar o HTML verá que a palavra *novamente* está dentro de duas tags `mark`.


----------

Você pode trabalhar com o `replace` utilizando `regex` e a flag *g*, com isso a substituição será efetuada em todas as palavras encontradas.

Sua função `marcarTexto_adverbio` ficaria mais ou menos da seguinte maneira.

    function marcarTexto_adverbio(target) {
        $("#content").html(function (_, html) {
            return html.replace(new RegExp(target, "g"), '<mark>' + target + '</mark>')
        });
    }

Isso vai criar as tags `mark` em todas as palavras, porém como existem palavras repetidas, algumas pode ter duas taks `mark` ou até mais.

Para corrigir isso, podemos optar por colocar as palavras já substituídas em um `Map`, veja um exemplo:

    var palavrasReplace = new Map();
    
    while (resultado = exp.exec(target)) {
      const palavra = resultado[0];
    
      if (!palavrasReplace.has(palavra)) {
        marcarTexto_adverbio(palavra); // função que coloca uma tag <mark> em volta
        palavrasReplace.set(palavra, true);
      }
    };

----------

Veja o exemplo completo:

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function marcarTexto_adverbio(target) {
        $("#content").html(function (_, html) {
            return html.replace(new RegExp(target, "g"), '<mark>' + target + '</mark>')
        });
    }

    function teste() {
      var target = $("#content").text();
      var exp = /\w+mente/g; // regex ok
      var resultado = null;

      var palavrasReplace = new Map();

      while (resultado = exp.exec(target)) {
        const palavra = resultado[0];

        if (!palavrasReplace.has(palavra)) {
          marcarTexto_adverbio(palavra); // função que coloca uma tag <mark> em volta
          palavrasReplace.set(palavra, true);
        }
      };
    }

<!-- language: lang-html -->

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <p id="content">novamente mais brevemente uma vez claro, claramente demente, igualmente. novamente.</p>

    <button onclick="teste()">Mark</button>

<!-- end snippet -->


----------

> Documentações:
> 
> https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/RegExp
> 
> https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/String/replace
> 
> https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Map
