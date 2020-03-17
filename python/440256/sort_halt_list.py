values = [7,6,5,4,3,2,1]

aux = values[0:5]
aux.sort()
aux += values[5:]
values = aux

print(values)
