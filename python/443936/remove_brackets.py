#Pegar o retorno da função sorted e exibir os valores acessando o índice do array
raizes = [10, 5]

raizesParaExibir = sorted(raizes)

print(f"A função tem duas raízes reais, que são: {raizesParaExibir[0]} e {raizesParaExibir[1]}.")

#Ordenar o array raizes usando o método sort e então acessar o array pelo índice
raizes = [10, 5]
raizes.sort()

print(f"A função tem duas raízes reais, que são: {raizes[0]} e {raizes[1]}.")

#Transforma a lista em string e então remove os colchetes utilizando strip
raizes = [10, 5]

print(f"A função tem duas raízes reais, que são: {str(sorted(raizes)).strip('[]')}.")

#Transforma a lista em string e então remove os colchetes utilizando replace
raizes = [10, 5]

print(f"A função tem duas raízes reais, que são: {str(sorted(raizes)).replace('[', '').replace(']', '')}.")

#Utilizar do método join da string
raizes = [10, 5]

print(f"A função tem duas raízes reais, que são: {', '.join(map(lambda x: str(x), sorted(raizes)))}.")
