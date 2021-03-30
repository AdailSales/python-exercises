#!python3
PI = 3.14
raio = float(input('Informe o raio da circunferência: '))

# print (type(raio))

# area = PI * raio * raio (Pode substituir esta equação pela linha a seguir:)
area = PI * pow(raio, 2)
print (f'A área da circunferência é {area}m².')
