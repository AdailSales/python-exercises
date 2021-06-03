'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

count_major = 0
count_minor = 0

for weight in range(1, 6):
    weight_value = float(input(f'Digite o peso da {weight}ª pessoa: '))
    
    if weight == 1:
        count_major = weight_value
        count_minor = weight_value
    else:
        if weight_value > count_major:
            count_major = weight_value
        if weight_value < count_minor:
            count_minor = weight_value
print(f'O maior peso lido foi de {count_major} kg.')
print(f'O menor peso lido foi de {count_minor} kg.')
