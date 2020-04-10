#Solicito o número
num = input()

#Transformo o número digitado em uma lista
num = list(num)

#Faço a orndenação inversa da lista, aqui eu já teria um resultado bem próximo
num.reverse()

#Converto a lista para uma string e depois para inteiro, isso removerá o zero a esquerda
num = int("".join(num))

#Exibo o número
print(num, "\n")
