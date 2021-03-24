#!usr/bin/python3

# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = ((9 * celsius) / 5) + 32
print(f'\nA temperatura de {celsius}ºC corresponde a {fahrenheit}ºF.\n')

