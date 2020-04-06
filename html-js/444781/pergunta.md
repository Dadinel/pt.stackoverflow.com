

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function validar() {
    	if (form.nome.value == "") {
    		document.getElementById("erro").innerHTML = "Por favor, preencha o campo nome.";
    		document.getElementById("erro").style.color = "red";

    		return false;
    	}

    	
    	if (form.senha.value.lenght > 0 && form.senha.value.lenght < 3) {
    		var erro = document.getElementById('errosenha');
    		erro.innerHTML="senha fraca";
    		erro.style.color="red";
    		return false;
    	} else if (form.senha.value.lenght >= 3 && form.senha.value.lenght < 5) {
    		var erro = document.getElementById('errosenha');
    		erro.innerHTML = "senha média";
    		erro.style.color = "orange";
    		return false;
    	} else if (form.senha.value.lenght = "") {
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
    	<script src="e1a.js"></script>
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

