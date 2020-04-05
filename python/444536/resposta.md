Sim, é possível e devem existir inúmeras formas de fazer isso.

Uma delas e bem simples, é criar uma função que contém a lógica onde você solicita os números ao usuário e adiciona na lista.


----------

Criamos a função, `listAppend`, que vai receber a lista para adicionar os números que o usuário informar e também recebe um número em relação qual é a lista, isso é somente para imprimir 1º lista, 2º lista etc:

    def listAppend(vector, number):
      for a in range(1, 11):
          vector.append(int(input(f'Digite o {a}° elemento da {number}° lista: ')))
      print('='*40)

Veja que é praticamente o mesmo código que você escreveu três vezes, mas agora isolado em uma função.

Agora que temos essa função, podemos apenas chamar ela para cada lista:

    listAppend(n1, 1)
    listAppend(n2, 2)
    listAppend(n3, 3)


----------

Seu código então ficaria da seguinte forma:

    def listAppend(vector, number):
      for a in range(1, 11):
          vector.append(int(input(f'Digite o {a}° elemento da {number}° lista: ')))
      print('='*40)
    
    n1 = list()
    n2 = list()
    n3 = list()
    n4 = list()
    
    listAppend(n1, 1)
    listAppend(n2, 2)
    listAppend(n3, 3)
    
    for d in range(0, 10):
        n4.append(n1[d])
        n4.append(n2[d])
        n4.append(n3[d])
    
    print(f'Intercalando as listas 1, 2 e 3 temos:\n'
          f'{n4}')

> Veja online: https://repl.it/repls/LowestWorthwhileEditor
