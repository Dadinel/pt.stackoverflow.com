Quando clica no botão ele muda o background da tag BODY, preciso que quando recarregar a página ele mantem a cor que ficou selecionada antes, acho que com localstorage funcione mas não entendo muita coisa disso.

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function mudarNome3(){   
     var element = document.body;  element.classList.toggle("dark-mode");
     
     if(document.getElementById("buttonmodoclaro").value == "MODO CLARO")
     {
      document.getElementById("buttonmodoclaro").value = "MODO ESCURO";
     } 
     else
     {
      document.getElementById("buttonmodoclaro").value = "MODO CLARO";
     }
    }

<!-- language: lang-css -->

    .dark-mode {
      background-color: black;
      color: white;
    }

    .dark-mode #buttonmodoclaro {
        color: white;
        font-weight: bold;
        border: 1px solid #a0a0a0;
        box-shadow: 0 0 4px 0 #8e8e8e inset;
    }

    #buttonmodoclaro{
        
        padding: 6px;
        border: 1px solid #561010;
        border-radius: 6px;
        margin-left: 21px;
        cursor: pointer;
        box-shadow: 0 0 6px 0 #171717 inset;
        color: red;
        background: none;
        font-variant: all-small-caps;
        font-family: sans-serif;
        font-size: 14px;
    }

<!-- language: lang-html -->

    <input type='button' id='buttonmodoclaro' onclick='mudarNome3();' value='MODO CLARO'>

<!-- end snippet -->

