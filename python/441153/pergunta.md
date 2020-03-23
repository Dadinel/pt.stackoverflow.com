Estou criando um script simples com uma `def` que imprimi um menu personalizado. O primeiro parâmetro é o cabeçalho, seguido pelo número de itens acessíveis pelo menu e finalmente um terceiro parâmetro que é desempacotado na função, representando as chamadas do menu.
É apenas um treino, nada tão útil assim, mas sinto que o que está sendo entregue não é a solução mais elegante, apesar de simplificar bastante. Pode haver uma confusão com o número de itens e todos os elementos digitados para o último parâmetro.
Alguém tem alguma idéia melhor? Talvez com um nível de complexidade maior ou mais elegante, funcional, etc.. Ou acham que para a solução proposta seria isso mesmo? 
Segue o script:

    def personalizado(txt, itens, *chamadas):
        print('-=-' * 15)
        print(txt.center(45))
        print('-=-' * 15)
        print()
        for c in range(0, itens):
            print(f'{c +1} - {chamadas[c]}')
    
    
    # teste protegido
    if __name__ == '__main__':
        personalizado('MENU QUALQUER', 6, 'Acessar', 'Visualizar', 'Cadastrar',
                      'Deletar', 'Reiniciar', 'Exit',)

O resultado:

    -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
                    MENU QUALQUER                
    -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
    
    1 - Acessar
    2 - Visualizar
    3 - Cadastrar
    4 - Deletar
    5 - Reiniciar
    6 - Exit
