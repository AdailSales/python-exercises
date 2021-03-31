'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
sen, cosseno e tangente desse ângulo.

'''

from math import radians, sin, cos, tan
angle = float(input('Digite um valor para o ângulo que você deseja: '))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
print(f'O ângulo de {angle:.0f} tem o seno de {sine:.2f}, o cosseno no valor de {cosine:.2f} e a tangente de {tangent:.2f}.')

