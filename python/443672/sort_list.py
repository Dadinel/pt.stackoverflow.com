numeros = []

for i in range(0,3):
    numeros.append(int(input('Digite um numero: : ')))

numeros.sort()
numeros.reverse()

print('a ordem eh:',numeros)

#--------------------------------------------------------

numeros = []

for i in range(0,3):
    numeros.append(int(input('Digite um numero: : ')))

numeros.sort(reverse=True)

print('a ordem eh:',numeros)

#--------------------------------------------------------

numeros = []

for i in range(0,3):
    numeros.append(int(input('Digite um numero: : ')))

print('a ordem eh:',sorted(numeros, reverse=True))
