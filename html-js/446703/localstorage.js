function restauraSalvo() {
  //Recupero o valor salvo no localStorage
  let valorSalvo = localStorage.getItem("dark-mode");

  //Se existir valor e for diferente do atual, troco...
  if (valorSalvo && valorSalvo !== document.getElementById("buttonmodoclaro").value)
  {
    mudarNome3();
  }
}

function mudarNome3(){   
  var element = document.body;

  element.classList.toggle("dark-mode");

  const botaoModo = document.getElementById("buttonmodoclaro");

  if(botaoModo.value == "MODO CLARO")
  {
    botaoModo.value = "MODO ESCURO";
  } 
  else
  {
    botaoModo.value = "MODO CLARO";
  }

  //Após efetuar a troca, salvo no localStorage
  localStorage.setItem("dark-mode", botaoModo.value);
}

restauraSalvo();
