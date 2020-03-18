let numero1 = '1,10';
numero1 = parseFloat(numero1.replace(/[^0-9,]*/g, '').replace(',', '.'));
let numero2 = '2,20';
numero2 = parseFloat(numero2.replace(/[^0-9,]*/g, '').replace(',', '.'));
let total = Math.round(numero1 + numero2);
console.log(total);
