function breakString(string, size) {
  //Valor default de 5000
  size = size || 5000;

  let breakStr = [];

  while (string.length > 0) {
    breakStr.push(string.substring(0,size));
    string = string.substring(size,string.length);
  }

  return breakStr;
}

let bigString = "abcdefghij".repeat(2000);

//Quebrar com o tamanho padrão de  5000
console.log(breakString(bigString));

//Quebrar de 130 em 130...
console.log(breakString(bigString, 130));

//Exemplo para verificar se a string de entrada é a mesma de saída
console.log( bigString == breakString(bigString, 147).reduce( (acc, value) => acc += value , "") );
