'''
Fazer um programa para ler as medidas da base e altura de um retângulo.
Em seguida mostrar o valor da área, perímetro e diagonal deste retângulo, com quatro casas decimais conforme exemplo.

Exemplo 1
Base do retângulo: 4.0
Altura do retângulo: 5.0
Área: 20.0000
Perímetro: 18.0000
Diagonal: 6.4031

Exemplo 2
Base do retângulo: 10.3
Altura do retângulo: 13.1
Área: 134.9300
Perímetro: 46.8000
Diagonal: 16.6643

criar as varáveis:
    base, altura, area, perimetro, diagonal: real
    base <- input
    altura <- input
    area <- base * altura
    perimetro <- 2*(base + altura)
    diagonal <- raizQ((base ** 2) + (altura ** 2))

'''
import math

rectangle_base = float(input('Digite o valor da base do retângulo: '))
rectangle_height = float(input('Digite o valor da altura do retângulo: '))
area = rectangle_base * rectangle_height
perimeter = 2 * (rectangle_base + rectangle_height)
diagonal = (math.sqrt((rectangle_base ** 2) + (rectangle_height ** 2)))
print(f'Área = {area:.4f}\n'
      f'Perímetro = {perimeter:.4f}\n'
      f'Diagonal = {diagonal:.4f}\n'
    )

