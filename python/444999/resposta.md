Acontece que você definiu dois métodos `set_nome`, um está trocando o valor da propriedade `__nome ` e o outro da propriedade `__sobrenome`:

    def set_nome(self,novo_nome):
        self.__nome = novo_nome
    def set_nome(self,novo_sobrenome):
        self.__sobrenome = novo_sobrenome

Com isso ao chamar o método set_nome:

    a.set_nome('ovo')

Na verdade quem está sendo atualizada é a propriedade `__sobrenome`


----------

Você pode corrigir o nome do método `set_nome` que atualiza a propriedade `__sobrenome` para `set_sobrenome`, corrigindo assim a situação:

    def set_sobrenome(self,novo_sobrenome):
        self.__sobrenome = novo_sobrenome


----------

Veja o exemplo com o seu código completo:

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

> Veja online: https://repl.it/repls/DirtyLimegreenThings
