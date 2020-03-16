Você pode criar o evento `onmouseover` assim que criar a `div`:

    squareElement.onmouseover = function() {
      this.style.backgroundColor = getRandomColor();
    }


----------

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    let btnCriar = document.querySelector('#btnCriar');
    let btnMudarCor = document.querySelector('#btnMudarCor');

    btnCriar.onclick = function createSquare() {
        let squareElement = document.createElement('div');
      
        squareElement.setAttribute('class', 'box');
        squareElement.style.width = "30px";
        squareElement.style.height = "30px";
        squareElement.style.backgroundColor = 'red';

        squareElement.onmouseover = function() {
          this.style.backgroundColor = getRandomColor();
        }

        document.body.appendChild(squareElement);
    }

    function getRandomColor() {

        let letters = "0123456789ABCDEF";
        let color = "#";

        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }

        return color;
    }

    btnMudarCor.onclick = function mudaCor() {
        let inputElement = document.getElementsByClassName('box');

        for(let i = 0; i< inputElement.length; i++){
            inputElement[i].style.backgroundColor = getRandomColor();
        }
    }

<!-- language: lang-css -->

    div {
      width: 30px;
      height: 30px;
      margin: 1rem;
    }

<!-- language: lang-html -->

    <button class='botao' id='btnCriar'>Criar Quadrado</button>
    <button class='botao' id='btnMudarCor'>Mudar Cor</button>

<!-- end snippet -->

