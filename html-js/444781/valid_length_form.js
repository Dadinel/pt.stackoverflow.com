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
