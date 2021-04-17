'''
Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro.
Os números podem ser digitados em qualquer ordem.

Exemplo 1:
Digite dois números inteiros:
6
24
São múltiplos

Exemplo 2:
Digite dois números inteiros:
24
6
São múltiplos
'''
print('Digite dois números inteiros:')
number_x = int(input(' '))
number_y = int(input(' '))

if number_x % number_y == 0 or number_y % number_x == 0:
    print('São múltiplos.')
else:
    print('Não são múltiplos.')
