#usr/bin/python3
'''
Escreva um programa que leia um valor em metros e o exiba convertido centímetros e milímetros.

'''
medida = float(input('Digite uma distância em metros: '))
metros = medida * 100
milimetros = medida * 1000

print(f'A medida de 25{medida:.0f}m corresponde a {metros:.0f}cm e {milimetros:.0f}mm.')
