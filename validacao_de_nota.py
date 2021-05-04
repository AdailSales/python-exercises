'''
(adaptado de URI 1117)Faça um programa que leia as notas referentes às duas avaliações de um aluno.
Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). 
Cada nota deve ser validada separadamente.

Exemplo 1: 
Digite a primeira nota: 3.5
Digite a segunda nota: 10.0
MEDIA = 6.75 

Exemplo 2:
Digite a primeira nota: -3.5
Valor invalido!
Tente novamente: 3.5
Digite a segunda nota: 11.0
Valor invalido!
Tente novamente: 10.5
Valor invalido!
Tente novamente: 10.0
MÉDIA = 6.75
'''

primeira_nota = float(input('Digite a primeira nota: '))

while primeira_nota < 0 or primeira_nota > 10:
    print('Valor inválido!')
    primeira_nota = float(input('Tente novamente: '))


segunda_nota = float(input('Digite a segunda nota: '))

while segunda_nota < 0 or segunda_nota > 10:
    print('Valor inválido!')
    segunda_nota = float(input('Tente novamente: '))
    
media = (primeira_nota + segunda_nota) / 2
print(f'MÉDIA = {media:.2f}')
