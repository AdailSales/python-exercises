#!usr/bin/python
'''
b1, b2, h, area : real
b1 <- digitar o valor
b2 <- digitar o valor
h <- digitar o valor

area <- (b1 + b2) / 2.0 * h;

escreval(area)
'''
b1 = float(input('Digite um valor: '))
b2 = float(input('Digite outro valor: '))
h = float(input('Digite outro valor: '))
area = (b1 + b2) / 2.0 * h

print(area, '\n')

print(f'A área do trapézio é igual a {area}\n')
