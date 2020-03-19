Meu objetivo num post anterior era colocar um valor máximo e mínimo em um campo de texto, um usuário solucionou ele quase perfeitamente. Vamos utilizar como exemplo no máximo o número ```37```:

<!-- begin snippet: js hide: false console: true babel: null -->

<!-- language: lang-js -->

    function checa(e){
       const mi = +e.min;
       const ma = +e.max;
       const va = e.value;
       if(va < mi){
          e.value = mi;
       }else if(va > ma){
          e.value = ma;
       }
    }

<!-- language: lang-html -->

    <input oninput="checa(this)" value="1" type="number" min="1" max="37">

<!-- end snippet -->

Porém, caso o número máximo for por exemplo ```10```, ele não conseguirá apagar o número 1 para conseguir digitar por exemplo, um ```7```. Mas o número mínimo tem que ser 1, alguém saberia como ampliar essa solução?

Segue o link do post antigo: https://pt.stackoverflow.com/questions/440115/limitar-n%c3%bamero-num-input


