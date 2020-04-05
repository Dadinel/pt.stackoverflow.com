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
