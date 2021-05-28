# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

choose_number = int(input('Digite um número: '))
quantity = 0

for num in range(1, choose_number + 1):
    if choose_number % num == 0:
        print('\33[33m', end=' ')
        quantity += 1
    else:
        print('\33[31m', end=' ')
    print(f'{num}', end=' ' )
print(f'\nO número {choose_number} foi divisível {quantity} vezes', end='')
if quantity == 2:
    print(f', ele é divisível por 1 e por ele mesmo. \nPor isso, {choose_number} é um número primo.')
else:
    print(', e por isso ele NÃO é um número primo.')
