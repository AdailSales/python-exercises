'''
Desenvolva um programa que leia seis números inteiros e mostre a soma daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0
cont = 0

for value in range(1, 7):
    number = int(input(f'Digite o {value}º valor: '))
    if number % 2 == 0: 
        soma += number
        cont += 1
print(f'Vocẽ informou {cont} números e a soma foi {soma}.')
