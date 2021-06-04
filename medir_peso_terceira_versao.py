'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

list_of_weights = []

for weight in range(1,6):

    weight_value = float(input(f'Qual o peso da {weight}ª pessoa? '))

    list_of_weights += [weight_value]

list_of_weights.sort()

print(f'O maior peso lido foi de {list_of_weights[4]} Kg e o menor peso foi de {list_of_weights[0]} Kg.')
