O resultado `NaN` é devido a utilizado do `Math.round` em uma string.

Quando você utiliza o método `toFixed`, o retorno é uma string.

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    numero1 = '1,10';
    numero1 = parseFloat(numero1.replace(/[^0-9,]*/g, '').replace(',', '.'));
    numero2 = '2,20';
    numero2 = parseFloat(numero2.replace(/[^0-9,]*/g, '').replace(',', '.'));
    total = Math.round(numero1 + numero2);
    console.log(total);

<!-- end snippet -->

> Documentação: https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed
