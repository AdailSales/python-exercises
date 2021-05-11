'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
Faça o programa mostrar o tipo de triângulo que será formado:
- Equilátero: todos os lados são iguais;
- Isósceles: dois lados iguais;
- Escaleno: todos os lados diferentes;
'''
print('-' * 30)
print('Analisador de triângulos')
print('-' * 30)

first_segment = float(input('Digite o valor do primeiro segmento: '))
second_segment = float(input('Digite o valor do segundo segmento: '))
third_segment = float(input('Digite o valor do terceiro segmento: '))

if first_segment < second_segment + third_segment and second_segment < first_segment + third_segment and third_segment < first_segment + second_segment:
    if first_segment == second_segment and first_segment == third_segment:
        print(f'Os segmentos digitados {first_segment:.0f}, {second_segment:.0f} e {third_segment:.0f} podem formar um triângulo equilátero.')
    elif first_segment != second_segment and first_segment != third_segment and second_segment != third_segment:
        print(f'Os segmentos digitados {first_segment:.0f}, {second_segment:.0f} e {third_segment:.0f} podem formar um triângulo escaleno.')
    else:
        print(f'Os segmentos digitados {first_segment:.0f}, {second_segment:.0f} e {third_segment:.0f} podem formar um triângulo isósceles.')

else: 
    print(f'Os segmentos digitados {first_segment:.0f}, {second_segment:.0f} e {third_segment:.0f} NÃO podem formar triângulos.')

