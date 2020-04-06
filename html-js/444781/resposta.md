Existem alguns erros e por isso o código sempre acaba caindo no seu `else`.

A propriedade `lenght`, está com a escrita incorreta, o correto é `length`.

Além disso, você comparada o valor de `length` com uma string vazia, porém `length` é uma propriedade numérica:

    } else if (form.senha.value.length = "") {

Nesse trecho, podemos apenas remover o acesso a propriedade `length`, deixando da seguinte forma:

    } else if (form.senha.value == "") {

Caso queira utilizar o `length`, compare o mesmo com 0:

    } else if (form.senha.value.length == 0) {


----------

Corrigindo esses pontos, seu código ficará mais ou menos da seguinte forma:


<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function validar() {

    	if (form.nome.value == "") {
    		document.getElementById("erro").innerHTML = "Por favor, preencha o campo nome.";
    		document.getElementById("erro").style.color = "red";

    		return false;
    	}

    	if (form.senha.value.length > 0 && form.senha.value.length < 3) {
    		var erro = document.getElementById('errosenha');
    		erro.innerHTML="senha fraca";
    		erro.style.color="red";
    		return false;
    	} else if (form.senha.value.length >= 3 && form.senha.value.length < 5) {
    		var erro = document.getElementById('errosenha');
    		erro.innerHTML = "senha média";
    		erro.style.color = "orange";
    		return false;
    	} else if (form.senha.value.length == 0) {
    		var erro = document.getElementById('errosenha');
    		erro.innerHTML = "Por favor, preencha o campo senha.";
    		erro.style.color = "red";
    		return false;
      }  else{
      	var erro = document.getElementById('errosenha');
      	erro.innerHTML = "senha forte";
    		erro.style.color="green";
      }
      
    }

<!-- language: lang-html -->

    <!DOCTYPE html>
    <html>
    <head>
    	<title></title>
    	<meta charset="utf-8">
    </head>
    <body>
      <form name="form" onsubmit="return validar()" action="entrou.html">
        Nome: <input type="text" name="nome"> <span id="erro" ></span> <br><br> 
        Senha: <input type="password" name="senha"> <span id="errosenha"></span> <br><br>
        <input type="submit" value="enviar" >      
      </form>
    </body>
    </html>

<!-- end snippet -->

> Documentação sobre a propriedade `length` da string:

> https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/String/length
