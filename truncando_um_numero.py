#!usr/bin/python3
'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

Exemplo: Digite um número: 6.127
O número 6.127 tem a aparte inteira 6.
'''

from math import trunc
number = float(input('Digite um valor não inteiro: '))
integer_number = trunc(number)
print(f'O número {number} tem a parte inteira {integer_number}.')
