'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens de até 200km e R$ 0.45 para viagens mais longas.
'''
from time import sleep

distance = float(input('Digite a distância da viagem: '))
charge = distance * 0.50
charge2 = distance * 0.45

print(f'Você está prestes a começar uma viagem de {distance:.2f} Km.')
sleep(3)

if distance > 0 and distance <= 200:
    print(f'O valor total da viagem é de R$ {charge:.2f}')
elif distance > 200:
    print(f'O valor total da viagem é de R$ {charge2:.2f}')
else:
    print('Insira um valor maior que 0 para a distância da viagem.')
