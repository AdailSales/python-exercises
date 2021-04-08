'''
Fazer um programa para ler o valor "r" do raio de um círculo, e depois mostrar o valor da área do
círculo com três casas decimais. A fórmula da área do círculo é a seguinte: area = π.r² . Você pode
usar o valor de π fornecido pela biblioteca da sua linguagem de programação, ou então, se preferir, use
diretamente o valor 3.14159.

'''
from math import pi

radius = float(input('Digite o raio do círculo: '))
area = pi * (radius ** 2)
print(f'AREA = {area:.3f}')

