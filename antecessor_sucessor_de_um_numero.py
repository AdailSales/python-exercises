'''
numero = input de dados.
Saída:
Escreva("Analisando o valor {} seu antecessor é {} e seu sucessor é {})
'''
numero = int(input('Digite um número: '))

antecessor = numero - 1
sucessor = numero + 1

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format(numero, antecessor, sucessor))

