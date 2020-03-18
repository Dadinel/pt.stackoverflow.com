Porquê dois valores decimais retorna NaN ?

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    numero1 = '1,10';
    numero1 = parseFloat(numero1.replace(/[^0-9,]*/g, '').replace(',', '.')).toFixed(2); // output: 1.10
    numero2 = '2,20';
    numero2 = parseFloat(numero2.replace(/[^0-9,]*/g, '').replace(',', '.')).toFixed(2); // output: 2.20
    total = Math.round(numero1 + numero2); // output: NaN
    console.log(total);

<!-- end snippet -->

