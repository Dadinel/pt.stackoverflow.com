n = int(input("Digiteo número de termos:"))
soma = 0

for i in range(1, n+1):
  if i%2 > 0:
    soma += i

print(soma)
