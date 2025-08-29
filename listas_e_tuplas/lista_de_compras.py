lista_compras = []

while True:
    opcao = input('Selecione uma opção \n' \
    '[I]nserir [A]pagar [L]istar [S]air: ').lower()

    if opcao == 'i':
        item = input('Informe o que deseja inserir: ')
        lista_compras.append(item)

        for indice, descricao in enumerate(lista_compras):
         print(indice, descricao)
   
    elif opcao == 'a':
        indice = input('Informe o indice do item que deseja apagar: ')
        if indice.isdigit():
            indice = int(indice)
            if 0 <= indice and indice < len(lista_compras):
                lista_compras.pop(indice)
                print('Removido! Nova lista:')
                for indice, descricao in enumerate(lista_compras):
                    print(indice, descricao)
            else:
                print('Indice inválido.')
        else:
            print('Valor inválido, digite um número.')

    elif opcao == 'l':
        if lista_compras:
            print("Lista de compras:")
            for i, item in enumerate(lista_compras):
                print(f'{i} - {item}')
        else:
            print('A lista está vazia.')

    elif opcao == 's':
        print('Você saiu.')
        break

    else:
        print('Opção inválida!')
