'''
Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três números lidos. Em caso de empate, mostrar apenas uma vez. 

Exemplo 1:
Primeiro valor: 7
Segundo valor: 3
Terceiro valor: 8
MENOR = 3

Exemplo 2:
Primeiro valor: 5
Segundo valor: 12
Terceiro valor: 5
MENOR = 5

Exemplo 3:
Primeiro valor: 9
Segundo valor: 9
Terceiro valor: 9
MENOR = 9

'''
first = int(input('Digite o primeiro número: \n'))
second = int(input('Digite o segundo número: \n')) 
third = int(input('Digite o terceiro número: \n'))

minor = first

if second < minor:
    minor = second
if third < minor:
    minor = third

print ('Primeiro valor:', first, '\n'
       'Segundo valor:', second, '\n'
       'Terceiro valor:', third, '\n'
       'Menor:', minor)
