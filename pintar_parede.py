#!usr/bin/python3

width = float(input('Qual a largura da sua parede? '))
height = float(input('Agora digite qual a altura da sua parede: '))
area = width * height
print(f'\nSua parede tem a dimensão de {width}x{height} e sua área é de {area}m².')

ink  = area / 2
print(f'\nPara pintar essa parede, você precisará de {ink}l de tinta.')
