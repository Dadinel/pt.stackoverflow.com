class Nome:
    def __init__(self,nome,sobrenome):
        self.__nome = nome # variável privada
        self.__sobrenome = sobrenome # variável privada
        self.nome_completo = nome + ' ' + sobrenome # variável pública

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def set_nome(self,novo_nome):
        self.__nome = novo_nome

    def set_sobrenome(self,novo_sobrenome):
        self.__sobrenome = novo_sobrenome


a = Nome('Alan','Aragao')
a.set_nome('ovo')

print("Nome:", a.get_nome())
print("Sobrenome:", a.get_sobrenome())
