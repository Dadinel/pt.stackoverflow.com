O `localStorage` realmente pode lhe atender, você precisaria salvar o valor atual nele, ou seja, sempre que o botão for clicado e recuperar assim que a página for carregada.


----------


Seu JS ficaria mais ou menos da seguinte forma:

```javascript
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
```


A função `restauraSalvo` é invocada assim que a página é carregada e com isso traz o valor salvo no `localStorage` e atualiza para o mesmo caso seja necessário.

Já a função `mudarNome3` passa a salvar o valor atual no `localStorage` sempre é acionada.

> Veja online: https://repl.it/repls/PresentLustrousDesigner

*Obs: O `localStorage` não funciona no stacksnippets, por isso coloquei o exemplo em uma outra página.*

----------

> Documentação: https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
