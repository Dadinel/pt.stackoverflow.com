Você deve imprimir o número invertido seguido de um final de linha. Não é preciso imprimir o 0 mais a esquerda. Por exemplo, se o número digitado for 30, basta que você imprima 3 e não 03.

    num=int(input())
    if num > 0:
        a = num%10
        b = num//10%10
        d = str("%d%d"%(a, b))
        print(d)
    else:
        num_ajus = num_ajus *10 + d
        print(num_ajus)



Eu quero quando eu digito o 40 aparece 4 não 04.
