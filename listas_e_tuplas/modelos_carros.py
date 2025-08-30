#Uso basico de listas e tuplas

lista_carros = [
    ("Gol", 2010),
    ("Polo", 2022),
    ("Onix", 2021),
    ("Celta", 2008),
    ("Sandero", 2015),
    ("Corolla", 2019),
    ("Civic", 2024),
    ("HB20", 2018),
    ("Ka", 2017),
    ("Fiesta", 2014),
    ("Cruze", 2025),
]

while True:

    estado_carro = input('Informe o tipo de carro que quer ver \n [N]ovos [S]emi-novos [U]sados [F]inalizar: ').lower()

    if estado_carro == 'n':
        for carro, ano in lista_carros:
            if ano >= 2024:
                print(f'Modelo: {carro}, Ano {ano}')
    elif estado_carro == 's':
        for carro, ano in lista_carros:
            if ano >= 2021 and ano <=2023:
                print(f'Modelo: {carro}, Ano {ano}')
    elif estado_carro == 'u':
        for carro, ano in lista_carros:
            if ano <= 2020:
                print(f'Modelo: {carro}, Ano {ano}')
    elif estado_carro == 'f':
        print('Voce saiu. Obrigado!')
        break
    else:
        print('Valor invalido. Digite novamente.')