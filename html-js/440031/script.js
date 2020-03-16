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
