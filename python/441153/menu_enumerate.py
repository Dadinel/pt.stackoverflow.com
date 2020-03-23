def personalizado(txt, *chamadas):
    print('-=-' * 15, txt.center(45), '-=-' * 15, '', sep='\n')

    for index, chamada in enumerate(chamadas):
        print(f'{index + 1} - {chamada}')

    #list comprehension
    #[print(f'{index +1} - {chamada}') for index, chamada in enumerate(chamadas)]

    #join da string com quebra de linha
    #print('\n'.join(f'{index +1} - {chamada}' for index, chamada in enumerate(chamadas)))

# teste protegido
if __name__ == '__main__':
    personalizado('MENU QUALQUER', 'Acessar', 'Visualizar', 'Cadastrar',
                  'Deletar', 'Reiniciar', 'Exit')
