'''
No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual foi a maior.

Exemplo 1:
Digite as três distâncias:
83.21
79.53
89.15
MAIOR DISTÂNCIA = 89.15

Exemplo 2:
Digite as três distâncias:
83.21
87.20
83.21
MAIOR DISTÂNCIA = 87.20

'''

print('Digite as três distâncias:')
distance_1 = float(input(' '))
distance_2 = float(input(' '))
distance_3 = float(input(' '))

if distance_1 > distance_2 and distance_1 > distance_3:
    print('MAIOR DISTÂNCIA:', distance_1)
elif distance_2 > distance_3:
    print('MAIOR DISTÂNCIA:', distance_2)
else:
    print('MAIOR DISTÂNCIA:', distance_3)

