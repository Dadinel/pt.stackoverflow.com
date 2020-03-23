Você na verdade escreveu o valor de `n1` no HTML com o método `toFixed`, enquanto deveria ter feito isso com o método `toLocaleString`.

O uso do método `toLocaleString` está correto, porém você utilizou ele e não fez nada com o retorno.


<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    let n1 = 155551.15;

    document.write(`${n1.toLocaleString('pt-br', { style: 'currency', currency: 'BRL' })}`);

<!-- end snippet -->


O trecho do código com o `toFixed` não é necessário.
