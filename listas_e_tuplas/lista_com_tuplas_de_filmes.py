#Uso basico de listas e tuplas

lista_filmes = [
    ("O Poderoso Chefão", 1972),
    ("Matrix", 1999),
    ("Interestelar", 2014),
    ("Parasita", 2019),
    ("Top Gun: Maverick", 2022),
    ("Inception", 2010),
    ("Titanic", 1997),
    ("Avatar", 2009),
    ("Jurassic Park", 1993),
    ("Os Vingadores", 2012),
    ("O Senhor dos Anéis", 2001),
]

while True:

    faixa = input(
        'Informe o tipo de filme que quer ver \n [C]lássicos [R]ecentes [N]ovos [F]inalizar: ').lower()
    
    encontrados = []

    if faixa == 'f':
        print('Você saiu. Obrigado!')
        break

    for filme, ano in lista_filmes:
        if faixa == 'n' and ano >= 2020:
            encontrados.append((filme, ano))
        elif faixa == 'r' and 2000 <= ano <= 2019:
            encontrados.append((filme, ano))
        elif faixa == 'c' and ano < 2000:
            encontrados.append((filme, ano))
        
    if encontrados:
        print('Filmes encontrados: ')
        for filme, ano in encontrados:
            print(f'Filme: {filme}, Ano: {ano}')
    else:
            print('Nenhum filme foi encontrado. Tente outra faixa.')