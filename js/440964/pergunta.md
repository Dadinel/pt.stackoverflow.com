Estou tendo o seguinte problema : desejo realizar a contagem de quebras de linhas, ou seja, a quantide de **'\n'** em um arquivo. Para isso, desejo ao ler o arquivo tratá-lo como uma String. Estou tentando da seguinte maneira : 

        const fs = require('fs') 
        
        const contents = fs.readFileSync('<caminho para o arquivo>', 'uft-8')//permitir ler o arquivo desejado
        
        const matches = contents.match(/\n/g)//identifica o '\n' no arquivo
        
        const count = matches.length//indica a qtd de '\n' no arquivo
    
        console.log(count)

Estou recebendo a seguinte mensagem de erro : 

    **internal/fs/utils.js:85
        throw new ERR_INVALID_OPT_VALUE_ENCODING(encoding);
        ^
    TypeError [ERR_INVALID_OPT_VALUE_ENCODING]: The value "uft-8" is invalid for option "encoding"
        at assertEncoding (internal/fs/utils.js:85:11)
        at getOptions (internal/fs/utils.js:221:5)
        at Object.readFileSync (fs.js:357:13)
        at Object.<anonymous> (/home/gabriel_rc/Área de Trabalho/Curso de NodeJS/exercícios/3.js:10:21)
        at Module._compile (internal/modules/cjs/loader.js:1158:30)
        at Object.Module._extensions..js (internal/modules/cjs/loader.js:1178:10)
        at Module.load (internal/modules/cjs/loader.js:1002:32)
        at Function.Module._load (internal/modules/cjs/loader.js:901:14)
        at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:74:12)
        at internal/main/run_main_module.js:18:47 {
      code: 'ERR_INVALID_OPT_VALUE_ENCODING'
    }**

Como resolver isto?


