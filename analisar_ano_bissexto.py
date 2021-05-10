# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.


year = int(input('Digite o ano: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano de {year} é bissexto.')
else:
    print(f'O ano de {year} não é bissexto.')

