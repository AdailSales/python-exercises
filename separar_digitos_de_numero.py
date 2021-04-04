'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Exemplo:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1

'''
num = int(input('Digite um número com até quatro algarismos: '))
unid = num // 1 % 10
dezn = num //10 % 10
cent = num // 100 % 10
milhr = num // 1000 % 10

print(f'Analisando o número {num}.\n'
      f'Unidade: {unid};\n'
      f'Dezena: {dezn};\n'
      f'Centena: {cent};\n'
      f'Milhar: {milhr}.'
      )

