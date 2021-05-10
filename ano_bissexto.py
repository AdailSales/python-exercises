# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
import calendar

year = int(input('Digite o ano: '))

leap_year = calendar.isleap(year)

if year == 0:
    year = date.today().year
if leap_year is True:
    print(f'O ano de {year} é bissexto.')
else:
    print(f'O ano de {year} não é bissexto.')
