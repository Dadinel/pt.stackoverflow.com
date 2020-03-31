Tava resolvendo uma simples questão de Python 

O programa pede três números e retorna em ordem decrescente - 

Resolvi fazer usando uma lista, assim:

    numeros = []
    for i in range(0,3):
        numeros.append(int(input('Digite um numero: : ')))
        numeros.sort()
        numeros.reverse()
        
    print('a ordem eh:',numeros)

O programa funcionou, mas fiquei me perguntando  se essa resolução é 'aceitavél' aos olhos de um programador experiente. E se não, como fariam?
