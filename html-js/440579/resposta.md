No cenário do numero máximo ser 10, você pode alterar a função `checa` para permitir que o campo fique vazio, permitindo assim que o valor mínimo seja apagado e o valor 7 seja inserido:

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function checa(e){
       const mi = +e.min;
       const ma = +e.max;
       const va = e.value;

       if(va.length) {
          if(va < mi){
             e.value = mi;
          }else if(va > ma){
             e.value = ma;
          }
       }
    }

<!-- language: lang-html -->

    <input oninput="checa(this)" value="1" type="number" min="1" max="10">

<!-- end snippet -->


----------


Mas isso pode gerar um problema pra você, caso esse campo seja obrigatório!

Se o campo for obrigatório e estiver dentro de um `form`, você pode utilizar do atributo `required` no seu `input`:

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-html -->

    <form>
      <input type="number" min="1" max="10" required>
      <input type="submit">
    </form>

<!-- end snippet -->

Veja que se você deixar o campo vazio, o *submit* não permite o envio.


----------


Se seu campo não está dentro de um formulário e você precisa que ele tenha um valor, você pode implementar o evento `onblur` para que ao sair do campo, caso o mesmo esteja vazio, seja inserido um valor, podendo ser o valor mínimo:

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function checa(e){
        const mi = +e.min;
        const ma = +e.max;
        const va = e.value;

        if (va.length) {
            if(va < mi){
                e.value = mi;
            }else if(va > ma){
                e.value = ma;
            }
        }
    }

    function valorMinimo(e) {
        if (!e.value.length) {
            e.value = e.min;
        }
    }

<!-- language: lang-html -->

    <input oninput="checa(this)" onblur="valorMinimo(this)" value="1" type="number" min="1" max="10">

<!-- end snippet -->
