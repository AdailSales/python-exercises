'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os dez primeiros termos dessa progressão.
'''
first = int(input('Digite o primeiro termo: '))
ratio = int(input('Razão: '))
tenth = first + (11 -1) * ratio

for sequence in range(first, tenth, ratio):
    print(f'{sequence}', end=' -> ')
print('ACABOU')


