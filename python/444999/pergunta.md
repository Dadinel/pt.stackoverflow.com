Gostaria de saber onde está o erro nesse código supostamente simples
```
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
    def set_nome(self,novo_sobrenome):
        self.__sobrenome = novo_sobrenome


        
a = Nome('Alan','Aragao')
a.set_nome('ovo')
a.get_nome()
```

quando eu executo o código, o nome 'ovo' não é retornado, e sim o nome 'Alan'
