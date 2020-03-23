Uma sugestão, seria remover o segundo parâmetro (`itens`) da função `personalizado`, pois como você recebe no terceiro parâmetro uma tupla, você pode iterar nela e descobrir a quantidade, com isso, seu for poderia ficar assim:

    for index, chamada in enumerate(chamadas):
        print(f'{index + 1} - {chamada}')



Como exemplo, utilizando o `enumerate` para já ter acesso a índice.

----------

*Outras coisas que você pode fazer como aprendizado e testes seriam:*



Diminuir a quantidade de chamadas da função `print`, é possível utilizar o parâmetro `sep`, passando assim diversos parâmetros para ela e a separação seria uma quebra de linha:

    print('-=-' * 15, txt.center(45), '-=-' * 15, '', sep='\n')

Criar o loop em apenas uma linha:

    #list comprehension
    [print(f'{index +1} - {chamada}') for index, chamada in enumerate(chamadas)]

    #join da string que contém a quebra de linha
    print('\n'.join(f'{index +1} - {chamada}' for index, chamada in enumerate(chamadas)))


----------

Achei o uso do parâmetro `*chamadas` bem legal, a chamada da função fica mais simples, não tendo a necessidade de criar a lista.


----------

> Exemplo online: https://repl.it/repls/HelpfulPersonalPlan
