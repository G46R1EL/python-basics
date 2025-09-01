cpf_digitado = input('Digite um cpf para ser validado: ')

multiplicador = 10
soma_dos_multiplicados = 0
cpf_somente_numeros = ''

for num in cpf_digitado:
    if num.isdigit():
        cpf_somente_numeros += num

nove_digitos = cpf_somente_numeros[:9]

for num in nove_digitos:
    multiplicacao = int(num) * multiplicador
    soma_dos_multiplicados += multiplicacao
    multiplicador -= 1

valor_vezes_dez = soma_dos_multiplicados * 10
resto_por_onze = valor_vezes_dez % 11

if resto_por_onze > 9:
    valor_primeiro__digito = 0
else:
    valor_primeiro__digito = resto_por_onze

print(f'O primeiro digito validador do CPF é: {valor_primeiro__digito}')

dez_digitos = nove_digitos + str(valor_primeiro__digito)

multiplicador = 11
soma_dos_multiplicados = 0

for num in dez_digitos:
    multiplicacao = int(num) * multiplicador
    soma_dos_multiplicados += multiplicacao
    multiplicador -= 1

valor_vezes_dez = soma_dos_multiplicados * 10
resto_por_onze = valor_vezes_dez % 11

if resto_por_onze > 9:
    valor_segundo__digito = 0
else:
    valor_segundo__digito = resto_por_onze

print(f'O segundo digito validador do CPF é: {valor_segundo__digito}')

cpf_gerado = dez_digitos + str(valor_segundo__digito)

if cpf_somente_numeros == cpf_gerado:
    print('O CPF digitado é válido!')
else:
    print('O CPF digitado é inválido!')