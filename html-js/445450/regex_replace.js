function marcarTexto_adverbio(target) {
    $("#content").html(function (_, html) {
        return html.replace(new RegExp(target, "g"), '<mark>' + target + '</mark>')
    });
}

function teste() {
  var target = $("#content").text();
  var exp = /\w+mente/g; // regex ok
  var resultado = null;

  var palavrasReplace = new Map();

  while (resultado = exp.exec(target)) {
    const palavra = resultado[0];

    if (!palavrasReplace.has(palavra)) {
      marcarTexto_adverbio(palavra); // função que coloca uma tag <mark> em volta
      palavrasReplace.set(palavra, true);
    }
  };
}
