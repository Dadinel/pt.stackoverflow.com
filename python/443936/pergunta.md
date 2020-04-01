Estava criando uma calculadora de função quadrática e queria dispor as raízes na ordem crescente. Pesquisando, cheguei à função `sorted()`.

    raiz1 = round((-b + math.sqrt(delta)) / (2 * a), 2)
	raiz2 = round((-b - math.sqrt(delta)) / (2 * a), 2)

	raizes = [raiz1, raiz2]

    if delta > 0:
    	print(f"A função tem duas raízes reais, que são: {sorted(raizes, key=int)}.")

O resultado disso é que vou ter as raízes dentro de colchetes, ao invés de parênteses, como é o padrão. Eu sei que isso não é grande problema, mas eu penso que no futuro haverão situações em que eu não vou querer os números dentro de colchetes, por isso eu gostaria de saber se tem algum jeito de suprimi-los.
