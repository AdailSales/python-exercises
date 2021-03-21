#!usr/bin/python3
import math
'''
Escreva(numero)
saída:
    Escreval('O dobro de {numero} vale {dobro}')
    Escreval('O triplo de {numero} vale {triplo}')
    Escreval('A raiz quadrada de {numero} vale {raiz_quadrada}')
'''

number = int(input('Digite um número: '))
double = number * 2
triple = number * 3
square_root = math.sqrt(number)

print(f'O dobro de {number} vale {double}\n'
      f'O triplo de {number} vale {triple}\n'
      f'A raiz quadrada de {number} vale {square_root:.2f}\n')

'''
num = int(input('Digite um número: '))
print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}.'.format(num, (num*2), num, (num*3), num, (num**(1/2))))
'''
'''
num = int(input('Digite um número: '))
print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}.'.format(num, (num*2), num, (num*3), num, pow(num, (1/2))))
'''
