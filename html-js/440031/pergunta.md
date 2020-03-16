Boa noite amigos, eu criei um código que toda vez que um botão é pressionado ele cria uma div... O problema é que eu preciso criar um modo usando querySelector e onmouseover, para, sempre que o mouse passar por cima de alguma dessas div ele troque a cor para outra aleatória, como faço pois sempre que inicio o código as divs ainda não existem, como eu as referencio para saber qual delas o mouse passou por cima?

Como podem ver eu consegui fazer com um botão mudar cor, mas o intuito é não ter botão.

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    let btnCriar = document.querySelector('#btnCriar');
    let btnRemover = document.querySelector('#btnRemover');
    let btnMudarCor = document.querySelector('#btnMudarCor');
    let nomes = ['Diego', 'Gabriel', 'Lucas'];

    btnCriar.onclick = function createSquare() {

        let squareElement = document.createElement('div')
        squareElement.setAttribute('class', 'box');
        squareElement.style.width = 100;
        squareElement.style.height = 100;
        squareElement.style.backgroundColor = 'red';

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

