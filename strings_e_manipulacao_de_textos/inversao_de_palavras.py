# Exercício simples para inverter as letras de uma palavra

while True:

    selecao = input('Esse programa inverte palavras. Digite "I" para inverter uma palavra/frase ou digite "S" para sair: ')

    if selecao.lower() == "i":
        
        palavra_inicial = input('Insira uma palavra e ela será invertida: ')

        palavra_nova = ''

        for i in palavra_inicial:
            palavra_nova = i + palavra_nova

        print(f'A palavra invertida fica: {palavra_nova} \n')

        #Outra forma
        palavra_nova = palavra_inicial[::-1]

        print(f'Forma mais simples de inversão: {palavra_nova}')
        
    
    elif selecao.lower() == "s":

        print('Você saiu. Obrigado!')
        break

    else:
        print('Comando inválido!')
