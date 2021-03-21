#!usr/bin/python3

'''
Escreva algo.
A saída deve indicar:
    o tipo primitivo --> type()
    se tem só espaços --> isspace()
    se é um número --> isnumeric()
    se é alfabético --> isalpha()
    se é alfanumérico --> isalnum()
    se está em maiúscula --> isupper()
    se está em minúscula e --> islower()
    se está capitalizada --> istitle()
'''
nome_digitado = input('Digite algo: ')

'''
print('O tipo primitivo desse valor é ', type(nome_digitado))
print('Só tem espaços? ', nome_digitado.isspace())
print('É um número? ', nome_digitado.isnumeric())
print('É alfabético? ', nome_digitado.isalpha())
print('É alfanumérico? ', nome_digitado.isalnum())
print('Está em maiúscula? ', nome_digitado.isupper())
print('Está em minúscula? ', nome_digitado.islower())

print(f'Está capitalizada? {nome_digitado.istitle()}\n')
'''

print(f'O tipo primitivo desse valor é {type(nome_digitado)}\n'
f'Só tem espaços? {nome_digitado.isspace()}\n'
f'É um número? {nome_digitado.isnumeric()}\n'
f'É alfabético? {nome_digitado.isalpha()}\n'
f'É alfanumérico? {nome_digitado.isalnum()}\n'
f'Está em maiúscula? {nome_digitado.isupper()}\n'
f'Está em minúscula? {nome_digitado.islower()}\n'
f'Está capitalizada? {nome_digitado.istitle()}\n')
