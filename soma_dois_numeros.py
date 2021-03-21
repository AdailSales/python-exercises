#!usr/bin/python3
# criar uma variável numero1, uma variável numero 2 e uma variável resultado.
# escreva um valor para numero1
# escreva uma valor para numero2
# somar numero1 com numero2
# saída com a mensagem: "A soma entre {numero1} e {numero2} é igual a {resultado}!

numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))

resultado = numero1 + numero2

# print('A soma entre {} e {} é igual a {}!'.format(numero1, numero2, resultado))

print(f'A soma entre {numero1} e {numero2} é igaual a {resultado}!')
