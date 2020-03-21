const fs = require('fs');

const contents = fs.readFileSync('myfile.txt', 'utf8');//permitir ler o arquivo desejado

const matches = contents.match(/\n/g);//identifica o '\n' no arquivo

const count = matches.length;//indica a qtd de '\n' no arquivo

console.log(count);
