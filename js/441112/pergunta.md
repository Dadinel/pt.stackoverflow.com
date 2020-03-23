Como dividir um ```texto``` com ou mais de **20.000 caracteres** em partes iguais e cada parte contendo **5000 caracteres**? (NodeJs)

Tenho essa função: 

    textBreak = (data) => {
      const characterCounter = data.text.length;
      const pagesCounter = data.numpages;
      var text = data.text;
      var math = Math.round(characterCounter / pagesCounter) + 3000;
      var index = 0;
      var array = [];
      while (index < characterCounter) {
        array.push(text.substr(math, Math.min(index + math, text.length)));
        index += math;
      }
      console.log('textBreak: sucess');
      return { array, pagesCounter, characterCounter, math }
    }
    module.exports = textBreak;


