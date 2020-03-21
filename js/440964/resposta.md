Assim como o @Luiz Felipe citou nos comentários, você colocou o encoding errado, porém você fez isso duas vezes.

A primeira vez como `'uft-8'` conforme seu exemplo:

> ```none
TypeError [ERR_INVALID_OPT_VALUE_ENCODING]: The value "uft-8" is invalid for option "encoding"
> ```

E a segunda, como `'uft8'` conforme o erro que você colocou nos comentários:

> ```none
TypeError [ERR_INVALID_OPT_VALUE_ENCODING]: The value "uft8" is invalid for option "encoding"
> ```

Ambas as vezes você inverteu a sigla, o prefixo é **`utf`** e as duas vezes você escreveu <code>u<strong>f</strong>t</code>.

Portanto, a principal correção no seu código é:

    const contents = fs.readFileSync('myfile.txt', 'utf8');//permitir ler o arquivo desejado

Seu código então ficaria da seguinte forma:

    const fs = require('fs');
    
    const contents = fs.readFileSync('myfile.txt', 'utf8');//permitir ler o arquivo desejado
    
    const matches = contents.match(/\n/g);//identifica o '\n' no arquivo
    
    const count = matches.length;//indica a qtd de '\n' no arquivo
    
    console.log(count);

Vale a pena citar existe a possibilidade de exceção caso o arquivo não existe e caso o mesmo não possua uma quebra de linha, atualmente o código trabalha na certeza da existência do arquivo e na certeza que existe ao menos uma quebra de linha com `\n`.

> Veja este exemplo online: https://repl.it/repls/UnitedEsteemedRuntimeenvironment

> Documentação: https://nodejs.org/api/fs.html
