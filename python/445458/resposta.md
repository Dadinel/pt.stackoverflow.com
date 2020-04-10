Seguindo o seu código, basta converter o conteúdo da variável `d` para inteiro utilizando a função `int`, essa conversão já removerá o zero a esquerda, para efetuar uma quebra de linha, podemos utilizar o `"\n"`:

    num=int(input())
    
    if num > 0:
        a = num%10
        b = num//10%10
        d = int(str("%d%d"%(a, b)))
        print(d, "\n")
    else:
        num_ajus = num_ajus *10 + d
        print(num_ajus)


Veja online: https://repl.it/repls/WorstMellowNetworking

----------

Veja um outro exemplo de como fazer isso, sendo que dessa forma, podemos trabalhar com muito mais que dois números.

Transformando número em lista, invertendo a ordem , utilizando join para converter a lista em string e então converto para inteiro (remove o zero):

    #Solicito o número
    num = input()
    
    #Transformo o número digitado em uma lista
    num = list(num)
    #Faço a orndenação inversa da lista, aqui eu já teria um resultado bem próximo
    num.reverse()
    #Converto a lista para uma string e depois para inteiro, isso removerá o zero a esquerda
    num = int("".join(num))
    
    #Exibo o número e a quebra de linha
    print(num, "\n")

Veja online: https://repl.it/repls/SunnyQuerulousDevices
