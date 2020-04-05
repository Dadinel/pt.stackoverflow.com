 O problema que estou resolvendo é: Faça um Programa que leia três vetores com 10 elementos cada. Gere um quarto vetor de 30 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos três outros vetores. (Usando Listas)
 Eu consegui, porém gostaria de saber algum jeito para não precisar repetir o comando "for" três vezes assim como eu fiz no código abaixo: 

    
    n1 = list()
    n2 = list()
    n3 = list()
    n4 = list()
    
    for a in range(1, 11):
        n1.append(int(input(f'Digite o {a}° elemento da 1° lista: ')))
    print('='*40)
    
    for b in range(1, 11):
        n2.append(int(input(f'Digite o {b}° elemento da 2° lista: ')))
    print('='*40)
    
    for c in range(1, 11):
        n3.append(int(input(f'Digite o {c}° elemento da 3° lista: ')))
    print('='*40)
    
    for d in range(0, 10):
        n4.append(n1[d])
        n4.append(n2[d])
        n4.append(n3[d])
    
    print(f'Intercalando as listas 1, 2 e 3 temos:\n'
          f'{n4}')

