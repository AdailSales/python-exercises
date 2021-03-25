#!usr/bin/python3
'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

Exemplo: Digite um número: 6.127
O número 6.127 tem a aparte inteira 6.
'''

number = float(input('Digite um número não inteiro: '))
integer_number = int(number)
print(f'O número {number} tem a parte inteira {integer_number}.')
