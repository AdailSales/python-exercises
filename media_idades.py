'''
Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez, mostrar a mensagem "IMPOSSÍVEL CALCULAR".
Exemplo 1: 
Digite as idades:
31
27
46
-5
MEDIA = 34.67
Exemplo 2:
Digite as idades:
-10
IMPOSSÍVEL CALCULAR
'''
add = 0
count = 0

print('Digite as idades:')
age = int(input(' '))

while age >= 0:
    add = add + age
    count = count + 1
    age = int(input(' '))

if count == 0:
    print('IMPOSSÍVEL CALCULAR.')
else:
    media = add / count
    print(f'MÉDIA = {media:.2f}' )
